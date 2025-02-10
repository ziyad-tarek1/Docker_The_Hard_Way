# Use Python 3.9 base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app/

# Ensure logs directory exists
RUN mkdir -p /app/logs

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run Flask server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
