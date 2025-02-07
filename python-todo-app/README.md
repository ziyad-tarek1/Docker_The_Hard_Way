# Python Flask Todo App with MySQL

This is a simple Todo application built using **Python Flask** and **MySQL**. The application allows users to:

- View a list of tasks.
- Add new tasks.
- Mark tasks as complete.
- Delete tasks.

The application is containerized using **Docker** and **Docker Compose**, making it easy to set up and run.

![image](https://github.com/user-attachments/assets/d73f706c-a56c-46ed-a1c5-8e347ae8de15)

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Setup and Installation](#setup-and-installation)
4. [How It Works](#how-it-works)
5. [Usage](#usage)
6. [Directory Structure](#directory-structure)
7. [Troubleshooting](#troubleshooting)
8. [License](#license)

---

## Features

- **View Tasks**: Displays a list of all tasks.
- **Add Task**: Allows users to add a new task with a title and description.
- **Complete Task**: Marks a task as complete.
- **Delete Task**: Removes a task from the list.
- **Persistent Storage**: Uses MySQL to store tasks persistently.
- **Dockerized**: Easy to set up and run using Docker and Docker Compose.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/python-todo-app.git
   cd python-todo-app
   ```

2. **Build and Run the Application**:
   Use Docker Compose to build and start the application:
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**:
   Once the containers are running, open your browser and navigate to:
   ```
   http://localhost:5000
   ```

---

## How It Works

### Application Components

1. **Flask App**:
   - The Flask app serves the web interface and handles CRUD operations for tasks.
   - It connects to the MySQL database to store and retrieve tasks.

2. **MySQL Database**:
   - The MySQL database stores the `tasks` table, which contains the following fields:
     - `id`: Unique identifier for each task.
     - `title`: Title of the task.
     - `description`: Description of the task.
     - `is_complete`: Boolean flag to indicate if the task is complete.

3. **Docker Compose**:
   - The `docker-compose.yml` file defines two services:
     - `web`: The Flask app.
     - `db`: The MySQL database.
   - The `db` service uses a custom MySQL image that initializes the `tasks` table on startup.

### Workflow

1. When the application starts:
   - The MySQL container initializes the `tasks` table using the `init.sql` script.
   - The Flask app connects to the MySQL database and starts serving the web interface.

2. Users can:
   - View all tasks on the homepage.
   - Add a new task using the "Add Task" form.
   - Mark a task as complete by clicking the "Complete" button.
   - Delete a task by clicking the "Delete" button.

---

## Usage

### View Tasks

- Open the application in your browser at `http://localhost:5000`.
- The homepage displays a list of all tasks.

### Add a Task

1. On the homepage, fill out the "Add Task" form:
   - **Title**: Enter a title for the task.
   - **Description**: Enter a description for the task.
2. Click the "Add" button to save the task.

### Complete a Task

- On the homepage, click the "Complete" button next to a task to mark it as complete.

### Delete a Task

- On the homepage, click the "Delete" button next to a task to remove it.

---

## Directory Structure

```
python-todo-app/
├── app.py                       # Flask application
├── custom_mysql/                # Custom MySQL configuration
│   ├── Dockerfile               # Dockerfile for MySQL image
│   └── init.sql                 # SQL script to initialize the database
├── docker-compose.yml           # Docker Compose configuration
├── Dockerfile                   # Dockerfile for Flask app
├── requirements.txt             # Python dependencies
├── templates/                   # Flask templates
│   └── index.html               # HTML template for the homepage
└── README.md                    # Project documentation
```

---

## Troubleshooting

### Flask App Fails to Connect to MySQL

- Ensure the MySQL container is running:
  ```bash
  docker-compose logs db
  ```
- Check the database connection settings in `app.py` and `docker-compose.yml`.

### MySQL Container Fails to Start

- Ensure the `init.sql` script is correct and does not contain syntax errors.
- Check the MySQL logs for errors:
  ```bash
  docker-compose logs db
  ```

### General Issues

- Rebuild the Docker containers:
  ```bash
  docker-compose down
  docker-compose up --build
  ```


---

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [MySQL](https://www.mysql.com/) for the database.
- [Docker](https://www.docker.com/) for containerization.

---

Enjoy using the Todo App! If you have any questions or issues, feel free to open an issue or submit a pull request.

