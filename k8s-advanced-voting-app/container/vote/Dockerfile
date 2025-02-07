# Use the official Python runtime as a parent image
FROM python:3.11-slim
# Set the application directory
WORKDIR /app
# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt .
# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code
COPY . .
# Make port 80 available for links and/or publish
EXPOSE 80
# Define the command to run the application
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]