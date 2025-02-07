# Stage 1: Build stage
FROM node:16-alpine AS build
WORKDIR /app
# Copy package.json and package-lock.json first to leverage Docker layer caching
COPY package.json package-lock.json ./
# Install dependencies
RUN npm ci
# Copy the rest of the application files
COPY . .
# Build the application
RUN npm run build
# Stage 2: Final stage
FROM node:16-alpine
WORKDIR /app
# Set environment variables
ENV NODE_ENV=production
# Copy the built files, public directory, and src directory from the build stage
COPY --from=build /app/build ./build
COPY --from=build /app/public ./public
COPY --from=build /app/src ./src
# Copy package.json for production dependencies
COPY package.json ./
# Install only production dependencies
RUN npm install --production
# Expose the application port
EXPOSE 3000
# Health check to ensure the container is running
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/ || exit 1
# Start the application
CMD ["npm", "start"]