# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install -r ./requirments.txt

# Expose the port the app runs on
EXPOSE 5001

# Define the command to run the application when the container starts
CMD ["python", "app.py"]
