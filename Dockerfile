# Use the Python 3.10 base image
FROM python:3.10

# Set the PYTHONUNBUFFERED environment variable to 1
ENV PYTHONUNBUFFERED=1

# Working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project code to the working directory
COPY . .

# Expose port 8000 
EXPOSE 8000