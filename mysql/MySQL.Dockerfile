# MySQL.Dockerfile
FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=videodb
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password
COPY init.sql /docker-entrypoint-initdb.d/