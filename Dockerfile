# Use the official Python image as a base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port on which the application will run
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
