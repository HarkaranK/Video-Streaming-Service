# Use MySQL as the base image
FROM mysql:latest

# Optionally, set environment variables if needed
ENV MYSQL_ROOT_PASSWORD=yourpassword
ENV MYSQL_DATABASE=yourdatabase
ENV MYSQL_USER=youruser
ENV MYSQL_PASSWORD=yourpassword

# Copy your SQL initialization scripts if needed
# COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port if required
EXPOSE 3307

