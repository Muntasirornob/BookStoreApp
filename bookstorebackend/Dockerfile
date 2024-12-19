# Use Python as the base image
FROM  python:3.8.13-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app


# Copy the requirements file from the root to the container
COPY ./requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev && \
    pip install --no-cache-dir -r /app/requirements.txt && \
    pip install django django-cors-headers


# Copy the Django app
COPY . /app/

# Run migrations and start the server
EXPOSE 8000
