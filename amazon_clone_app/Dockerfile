# Stage 1: Build
FROM node:16-alpine AS build
# Set the working directory inside the container
WORKDIR /app
# Copy package.json and package-lock.json (or yarn.lock) to the container
COPY package*.json ./
# Install project dependencies
RUN npm install
# Copy the rest of the application code to the container
COPY . .
# Build the React app
RUN npm run build
# Stage 2: Production
FROM nginx:alpine
# Copy the build output to the Nginx html directory
COPY --from=build /app/build /usr/share/nginx/html
# Expose the port that the app will run on (usually 80 for Nginx)
EXPOSE 80
# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]