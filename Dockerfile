# ============================================================
# Dockerfile for Mocha Topia – Static Coffee Shop Website
# Base image: nginx:alpine (lightweight, ~40MB)
# Serves HTML/CSS/JS files via Nginx on port 80
# ============================================================

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
