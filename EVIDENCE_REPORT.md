# 📄 Dockerization & Verification Evidence Report
**Course / Assignment:** Week 6 — Containerization with Docker  
**Project Name:** Mocha Topia (Coffee Shop Web Application)  
**Author:** Faiz, Immanuel, Dwisasono  
**Date:** October 18, 2026  
**Git Branch:** `chore/dockerize-project`  
**Repository:** `mocha-topia`  

---

## 1. Executive Summary

This report provides the formal evidence of containerizing the **Mocha Topia** coffee shop web application in accordance with the Week 6 Docker Assignment requirements. 

The application was packaged into a lightweight, secure Docker image using **Nginx 1.27 on Alpine Linux**, orchestrated with **Docker Compose**, and verified across all functional paths (landing, registration, authentication, menu browsing, and cart management).

### Key Metrics:
* **Base Image:** `nginx:1.27-alpine`
* **Production Image Size:** **77.9 MB** (well below the typical 150MB+ Node/Ubuntu containers)
* **Container Port:** `80` (mapped to Host Port `8080`)
* **Verification Status:** **100% Passed (5 / 5 tests passed)**

---

## 2. Architecture & Runtime Rationale

### Why Nginx Alpine?
Mocha Topia is a client-side frontend web application built with HTML5, CSS3, JavaScript (ES6), and jQuery (loaded via CDN).

| Runtime Considered | Image Size | Security / Attack Surface | Appropriateness for Mocha Topia |
|---|---|---|---|
| **Ubuntu + Node.js** | ~500 MB | Large, includes unnecessary compilers & bash utilities | ❌ Overkill |
| **Node.js Alpine** | ~180 MB | Medium, contains JS runtime not needed for static HTML | ❌ Unnecessary |
| **Nginx 1.27 Alpine (Selected)** | **77.9 MB** | **Minimal, hardened, purpose-built HTTP server** | ✅ **Optimal Choice** |

---

## 3. Configuration Files Implementation

### A. Dockerfile (`Dockerfile`)
The Dockerfile uses a clean, single-stage Alpine build that removes default pages and injects custom performance & security configurations:

```dockerfile
# Step 1: Use a lightweight Nginx image as the base
FROM nginx:1.27-alpine

# Step 2: Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Step 3: Remove the default Nginx welcome page
RUN rm -rf ./*

# Step 4: Copy all website files into the Nginx html directory
COPY . .

# Step 5: Copy custom Nginx config for proper MIME types and caching
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Step 6: Expose port 80 (the port Nginx listens on inside the container)
EXPOSE 80

# Step 7: Start Nginx in the foreground (keeps the container running)
CMD ["nginx", "-g", "daemon off;"]
```

### B. Docker Ignore (`.dockerignore`)
Prevents sensitive files, version control overhead, and unnecessary assets from entering the build context:
```text
.git
.gitignore
.vscode
*.swp
*.swo
*~
Dockerfile
docker-compose.yml
compose.yaml
.dockerignore
.env
.env.*
!.env.example
*.md
*.pdf
Thumbs.db
.DS_Store
node_modules/
```

### C. Docker Compose (`compose.yaml`)
Enables reproducible single-command startup across team environments:
```yaml
services:
  app:
    build: .
    container_name: mocha-topia-app
    ports:
      - "8080:80"
    restart: unless-stopped
```

### D. Nginx Server Configuration (`nginx.conf`)
Optimized for static assets with Gzip compression and client-side caching:
```nginx
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location ~* \.(jpeg|jpg|png|gif|ico|css|js)$ {
        expires 7d;
        add_header Cache-Control "public, immutable";
    }

    location ~ /\. {
        deny all;
        access_log off;
        log_not_found off;
    }

    gzip on;
    gzip_types text/plain text/css application/javascript;
    gzip_min_length 256;
}
```

---

## 4. Verification Evidence & Test Results

### Verification Matrix

| Test ID | Test Category | Action / Command | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| **V-01** | Container Lifecycle | `docker ps` / `docker compose ps` | Status is `Up`, port `8080->80` | `Up`, mapped `0.0.0.0:8080->80/tcp` | ✅ **PASS** |
| **V-02** | Image Footprint | `docker image ls mocha-topia` | Image size is compact (< 100MB) | `77.9 MB` | ✅ **PASS** |
| **V-03** | HTTP Availability | `curl.exe -I http://localhost:8080` | Status Code `200 OK` | `HTTP/1.1 200 OK` | ✅ **PASS** |
| **V-04** | User Registration | Browser: Register Form | Client validation succeeds, account stored | User created successfully | ✅ **PASS** |
| **V-05** | User Login | Browser: Login Form | LocalStorage validates credentials | Redirects to Dashboard | ✅ **PASS** |
| **V-06** | Menu & Cart | Browser: Menu Page | Items added with price and quantity | Cart updates in real time | ✅ **PASS** |

---

## 5. Visual Proof (Screenshots of Containerized Execution)

All screenshots below were captured while running the application directly from the Docker container via `http://localhost:8080`.

### Evidence 1: Landing Page
The entry point loaded through the Nginx container at port 8080.
![Mocha Topia Landing Page](evidence/01_landing_page.png)

---

### Evidence 2: User Registration Flow
Client-side validation rules enforced with responsive feedback inside the container.
![User Registration Page](evidence/02_register_page.png)

---

### Evidence 3: Authentication / Login Flow
Credentials verified against stored profiles in `localStorage`.
![Login Page](evidence/03_login_page.png)

---

### Evidence 4: Main Dashboard & Coffee Menu
Catalog browsing, responsive frameset layout, and cart operations running smoothly inside Nginx.
![Dashboard and Menu](evidence/04_dashboard_menu.png)

---

## 6. Terminal Command Log Proof

### 1. Image Verification
```text
PS C:\Users\Lenovo\OneDrive\Documents\mocha-topia> docker image ls mocha-topia-app
REPOSITORY        TAG       IMAGE ID       CREATED        SIZE
mocha-topia-app   latest    11e3760d75f0   17 hours ago   77.9MB
```

### 2. Container Status Verification
```text
PS C:\Users\Lenovo\OneDrive\Documents\mocha-topia> docker ps --filter "name=mocha-topia-app"
CONTAINER ID   IMAGE               COMMAND                  STATUS          PORTS                                     NAMES
f73254a70c8a   mocha-topia:week6   "/docker-entrypoint.…"   Up 30 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mocha-topia-app
```

### 3. HTTP Server Response Header
```text
PS C:\Users\Lenovo\OneDrive\Documents\mocha-topia> curl.exe -I http://localhost:8080
HTTP/1.1 200 OK
Server: nginx/1.27.5
Date: Sun, 18 Oct 2026 04:54:19 GMT
Content-Type: text/html
Content-Length: 1133
Connection: keep-alive
```

---

## 7. How to Reproduce from Clean State

1. Clone repository:
   ```bash
   git clone <repository_url>
   cd mocha-topia
   ```
2. Build and launch:
   ```bash
   docker compose up --build -d
   ```
3. Verify status:
   ```bash
   docker compose ps
   ```
4. Access in web browser:
   ```
   http://localhost:8080
   ```
5. Teardown:
   ```bash
   docker compose down
   ```

---
*Report compiled automatically for Week 6 Docker Assignment verification.*
