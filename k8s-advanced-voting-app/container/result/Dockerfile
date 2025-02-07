# Base image
FROM node:18-slim AS base
# Set the working directory
WORKDIR /app
# Copy package.json and package-lock.json
COPY package*.json ./
# Install production dependencies
RUN npm ci --only=production \
 && npm cache clean --force
# Copy application code
COPY . .
# Set environment variable
ENV PORT 80
# Expose the port
EXPOSE 80
# Command to run the application
CMD ["node", "server.js"]
# Development stage
FROM base AS dev
# Install development dependencies
RUN npm install
# Install nodemon globally for development
RUN npm install -g nodemon
# Override the CMD for development
CMD ["nodemon", "server.js"]
# Production stage
FROM base AS prod
