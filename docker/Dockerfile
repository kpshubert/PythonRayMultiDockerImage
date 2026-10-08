FROM python:3.13-slim

WORKDIR /app

# Dependencies first so this layer is cached until requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Project code
COPY pyproject.toml .
COPY src/ src/
RUN pip install --no-cache-dir .

# No CMD/ENTRYPOINT: docker-compose.yml sets the head and worker commands
