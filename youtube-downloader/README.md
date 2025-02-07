# YouTube Downloader

A simple Flask-based web application to download YouTube videos or audio. This project uses `yt-dlp` to handle YouTube downloads and provides a user-friendly web interface.

![image](https://github.com/user-attachments/assets/6f5a3e97-4a71-418b-a5e4-ef85f884bb6c)

---

## Features

- Download YouTube videos in the best available quality.
- Download YouTube audio.
- Simple and intuitive web interface.
- Persist downloaded files outside the container using Docker volumes.

---

## Prerequisites

- Docker installed on your system.
- Basic knowledge of Docker commands.

---

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository-url>
cd youtube-downloader
```

---

### 2. Build the Docker Image

Build the Docker image for the YouTube Downloader:

```bash
docker build -t youtube-downloader .
```

---

### 3. Run the Container

You can run the container in two ways:

#### **Option 1: Using Port Mapping (Recommended for Most Users)**

This method maps the container's port to the host's port, making the application accessible via `localhost`.

```bash
docker run -p 5000:5000 -v /path/to/host/downloads:/app/Downloads youtube-downloader
```

- Replace `/path/to/host/downloads` with the directory on your host machine where you want to save downloaded files.
- Access the application at `http://localhost:5000`.

#### **Option 2: Using Host Network**

This method uses the host's network stack directly, which can help bypass certain network restrictions.

```bash
docker run --network host -v /path/to/host/downloads:/app/Downloads youtube-downloader
```

- Replace `/path/to/host/downloads` with the directory on your host machine where you want to save downloaded files.
- Access the application at `http://localhost:5000`.

---

### 4. Access the Application

Once the container is running, open your web browser and navigate to:

```
http://localhost:5000
```

---

### 5. Download YouTube Videos or Audio

1. Enter the YouTube video URL in the input field.
2. Select the download option:
   - **1**: Download video (best quality).
   - **2**: Download audio.
3. Click "Download".

The downloaded file will be saved in the directory you specified (e.g., `/path/to/host/downloads`).

---

## Project Structure

```
youtube-downloader/
├── app.py                  # Flask application
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── static/
│   └── styles.css          # CSS for the web interface
├── templates/
│   └── index.html          # HTML template for the web interface
└── README.md               # This file
```

---

## Customization

### Change Download Directory

To change the directory where downloaded files are saved, modify the `-v` flag in the `docker run` command. For example:

```bash
docker run -p 5000:5000 -v /custom/path:/app/Downloads youtube-downloader
```

---

## Troubleshooting

### 1. Connection Refused

If you cannot access the application at `http://localhost:5000`:
- Ensure the container is running (`docker ps`).
- Verify port mapping (`docker ps` should show `0.0.0.0:5000->5000/tcp`).


### 2. Debugging Inside the Container

Start an interactive shell inside the container:

```bash
docker exec -it <container_id> /bin/bash
```

---

## Advanced Usage



## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp): A feature-rich command-line tool for downloading YouTube videos.
- [Flask](https://flask.palletsprojects.com/): A lightweight web framework for Python.

---

Enjoy downloading YouTube videos with ease! 🎥🎶

