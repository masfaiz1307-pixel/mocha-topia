# ☕ Mocha Topia — Coffee Shop Website

> **"Bad mood? Reboot with coffee."**

Mocha Topia is a static coffee shop website featuring user registration/login, a menu catalog with cart functionality, a contact form, and a gallery — all built with HTML, CSS, JavaScript, and jQuery.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Docker Setup](#docker-setup)
- [Verification](#verification)
- [Logs & Status](#logs--status)
- [Stopping the App](#stopping-the-app)
- [Troubleshooting](#troubleshooting)
- [Known Limitations](#known-limitations)

---

## Project Overview

| Item                  | Details                                              |
|-----------------------|------------------------------------------------------|
| **Project Name**      | Mocha Topia                                          |
| **Technology Stack**  | HTML5, CSS3, JavaScript (ES6), jQuery 3.6.0          |
| **Web Server**        | Nginx 1.27 (Alpine)                                  |
| **Container Port**    | 80                                                   |
| **Host Port**         | 8080                                                 |
| **Core Features**     | User Registration/Login, Menu + Cart, Contact Form   |

### Main Features
1. **User Registration & Login** — Register with validation, login with localStorage-based authentication
2. **Coffee & Food Menu** — Browse drinks and food items, search, filter by category, add to cart with quantity selector
3. **Shopping Cart & Checkout** — View cart, adjust quantities, complete orders with delivery details
4. **Contact Form** — Send messages via FormSubmit with AJAX
5. **Gallery** — View café photos
6. **Navigation Sidebar** — Frameset-based layout with collapsible sidebar

---

## Prerequisites

- **Docker Desktop** version 28.x or later (tested on v28.5.1)
- **Docker Compose** version 2.x or later (tested on v2.40.2)
- **Git** for cloning the repository

### Verify Docker is installed:
```bash
docker version
docker compose version
```

---

## Getting Started

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd mocha-topia
```

### 2. Configure Environment Variables
This project is a static website and does **not** require any environment variables.
A `.env.example` file is included for documentation:
```bash
# No .env file needed — the app runs without environment variables
```

---

## Docker Setup

### Option A: Using Docker Compose (Recommended)

**Build and start:**
```bash
docker compose up --build -d
```

**Verify services are running:**
```bash
docker compose ps
```

### Option B: Using Docker CLI

**Build the image:**
```bash
docker build -t mocha-topia/website:week6 .
```

**Run the container:**
```bash
docker run -d --name mocha-topia-app -p 8080:80 mocha-topia/website:week6
```

### 3. Access the Application
Open your browser and go to:
```
http://localhost:8080
```

---

## Verification

After starting the container, verify the app works with these checks:

| Check | Action                                      | Expected Result                                 |
|-------|---------------------------------------------|-------------------------------------------------|
| V-01  | Run `docker ps` or `docker compose ps`      | Container status is `Up` / `running`            |
| V-02  | Open `http://localhost:8080` in browser      | Mocha Topia landing page loads with logo & buttons |
| V-03  | Register → Login → Browse Menu → Add to Cart | Full user flow completes successfully           |
| V-04  | Restart: `docker compose restart`            | App starts again and loads correctly            |

---

## Logs & Status

| Purpose                    | Command                                    |
|----------------------------|--------------------------------------------|
| List running containers    | `docker ps`                                |
| List all containers        | `docker ps -a`                             |
| Read container logs        | `docker logs mocha-topia-app`              |
| Follow logs continuously   | `docker logs -f mocha-topia-app`           |
| Inspect configuration      | `docker inspect mocha-topia-app`           |
| Open a shell               | `docker exec -it mocha-topia-app sh`       |
| View Compose status        | `docker compose ps`                        |
| Read Compose logs          | `docker compose logs`                      |

---

## Stopping the App

### Using Docker Compose:
```bash
docker compose down
```

### Using Docker CLI:
```bash
docker stop mocha-topia-app
docker rm mocha-topia-app
```

### Full cleanup (remove image too):
```bash
docker compose down --rmi all
```

---

## Troubleshooting

| Problem                          | Solution                                                              |
|----------------------------------|-----------------------------------------------------------------------|
| Port 8080 already in use         | Change the host port in `compose.yaml` (e.g., `9090:80`)            |
| Page not loading                 | Check `docker ps` to confirm container is running                    |
| Images not displaying            | Verify image files exist in the `images/` folder                     |
| Changes not appearing            | Rebuild: `docker compose up --build -d`                              |
| Container exits immediately      | Check logs: `docker logs mocha-topia-app`                            |

---

## Known Limitations

- **No persistent backend** — All user data (registration, cart, orders) is stored in the browser's `localStorage` and is not shared between browsers/devices.
- **No database** — This is a purely client-side application.
- **jQuery from CDN** — Requires internet access to load jQuery from `code.jquery.com`.
- **Frameset layout** — Uses HTML `<frameset>` which is deprecated in HTML5, but works in all major browsers.

---

## Project Structure

```
mocha-topia/
├── css/
│   └── style.css           # Main stylesheet
├── images/                  # Menu items and gallery photos
│   ├── logo.png
│   ├── Americano.jpeg
│   ├── cappucino.jpeg
│   └── ... (16 image files)
├── index.html               # Landing page
├── login.html               # Login form
├── register.html            # Registration form
├── frameset.html            # Main app layout (nav + content)
├── nav.html                 # Sidebar navigation
├── home.html                # Home page
├── menu.html                # Menu with cart functionality
├── cart.html                # Shopping cart & checkout
├── contact.html             # Contact form
├── contact-success.html     # Contact confirmation
├── about.html               # About page
├── gallery.html             # Photo gallery
├── dashboard.html           # User dashboard
├── welcome.html             # Welcome/landing page
├── forgot.html              # Password reset (demo)
├── logout.html              # Logout handler
├── purchase.html            # Order summary
├── Dockerfile               # Docker image configuration
├── .dockerignore            # Files excluded from Docker build
├── compose.yaml             # Docker Compose configuration
├── nginx.conf               # Custom Nginx server config
├── .env.example             # Environment variable template
└── README.md                # This file
```
