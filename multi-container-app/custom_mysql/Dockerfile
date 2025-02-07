# custom_mysql/Dockerfile
FROM mysql:latest

COPY init.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydb
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password