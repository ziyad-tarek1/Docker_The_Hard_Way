# Use a minimal base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only requirements file to leverage caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user for security
RUN useradd -m appuser

# Copy application code
COPY . .

# Create the logs directory and set proper permissions
RUN mkdir -p /app/logs && chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Expose the application port
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]