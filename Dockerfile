# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./app/alembic.ini /code/alembic.ini


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
