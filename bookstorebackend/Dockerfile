# Use Python as the base image
FROM  python:3.8.13-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies

RUN pip install django django-cors-headers

# Copy the Django app
COPY . /app/

# Run migrations and start the server
EXPOSE 8000
