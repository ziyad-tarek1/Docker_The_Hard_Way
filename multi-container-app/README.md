# Multi-Container Flask Application with MySQL & PostgreSQL

## Overview
This project is a multi-container Flask application that can connect to either MySQL or PostgreSQL databases using Docker. It includes Dockerfiles for custom MySQL and PostgreSQL images, a Flask application, and a `docker-compose.yml` file for simplified deployment.

## Project Structure
```
.
├── app.py
├── custom_mysql
│   ├── Dockerfile
│   └── init.sql
├── custom_postgres
│   ├── Dockerfile
│   └── init.sql
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Prerequisites
- Docker installed
- Docker Compose installed

## Build & Run Containers Individually

### Build Custom MySQL & PostgreSQL Images
```sh
docker build -t custom_mysql ./custom_mysql
docker build -t custom_postgres ./custom_postgres
```

### Run MySQL Container
```sh
docker run --name mysql_db \
    -e MYSQL_ROOT_PASSWORD=rootpassword \
    -e MYSQL_DATABASE=mydb \
    -e MYSQL_USER=user \
    -e MYSQL_PASSWORD=password \
    -p 3306:3306 -d custom_mysql
```

### Run PostgreSQL Container
```sh
docker run --name postgres_db \
    -e POSTGRES_USER=user \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_DB=mydb \
    -p 5432:5432 -d custom_postgres
```

### Build the Flask Application Image

```sh
docker build -t flask_app .
```

### Run Flask Application with MySQL
```sh
docker run --name flask_app_sql \
    --link mysql_db:db \
    -e DB_TYPE=mysql \
    -e MYSQL_DATABASE=mydb \
    -e MYSQL_USER=user \
    -e MYSQL_PASSWORD=password \
    -p 5000:5000 -d flask_app
```

### Run Flask Application with PostgreSQL
```sh
docker run --name flask_app \
    --link postgres_db:db \
    -e DB_TYPE=postgresql \
    -e POSTGRES_DB=mydb \
    -e POSTGRES_USER=user \
    -e POSTGRES_PASSWORD=password \
    -p 5000:5000 -d flask_app
```

## Using Docker Compose
A `docker-compose.yml` file is provided to simplify deployment.

### Start Services
```sh
docker-compose up -d
```

### Stop Services
```sh
docker-compose down
```

## Environment Variables
| Variable         | Description         |
|-----------------|---------------------|
| `DB_TYPE`       | Database type (`mysql` or `postgresql`) |
| `POSTGRES_DB`   | PostgreSQL database name |
| `POSTGRES_USER` | PostgreSQL username |
| `POSTGRES_PASSWORD` | PostgreSQL password |
| `MYSQL_DATABASE` | MySQL database name |
| `MYSQL_USER`    | MySQL username |
| `MYSQL_PASSWORD` | MySQL password |

## Accessing the Flask Application
Once the Flask app is running, you can access it at:
```
http://localhost:5000/
```

## Verifying Database Connection
If the application is running successfully, it should display:
```
Connected to DB!
```

## Cleanup
To remove all containers:
```sh
docker-compose down -v
```
To remove all images:
```sh
docker rmi custom_mysql custom_postgres flask_app
```

## Notes
- Ensure that ports 5000, 3306, and 5432 are available before running the containers.
- Modify `docker-compose.yml` to choose between MySQL and PostgreSQL.
- Database connection defaults to the `db` hostname as defined in `docker-compose.yml`.


