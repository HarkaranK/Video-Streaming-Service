# Use MySQL as the base image
FROM mysql:latest

# Optionally, set environment variables if needed
ENV MYSQL_ROOT_PASSWORD=vid
ENV MYSQL_DATABASE=video
ENV MYSQL_USER=vid
ENV MYSQL_PASSWORD=vid

# Copy your SQL initialization script into the MySQL initialization directory
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port if required
EXPOSE 3306


