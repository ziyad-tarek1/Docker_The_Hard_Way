# Dinosaur Game
- **Description**: A clone of the Chrome Dino game, containerized with Docker and Nginx.
- **Files**:
  - `Dockerfile`
  - `index.html`, `index.css`, `index.js`
  - `nginx.conf`
- **How to Run**:
  ```bash
  docker build -t dino-game .
  docker run -p 80:80 dino-game
  ```

- **Open your web browser and navigate to `http://localhost:8080` to view the analog clock.**

![image](https://github.com/user-attachments/assets/67f5fb23-66b6-4b18-bdf7-1be525595d05)
