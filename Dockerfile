# # FROM python:3.10-slim

# WORKDIR /app

# COPY . .

# RUN pip install --no-cache-dir -r requirements.txt

# ENV PYTHONUNBUFFERED=1

# CMD ["python", "inference.py"]


# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of project
COPY . .

# Avoid buffering (important for logs)
ENV PYTHONUNBUFFERED=1

# Run your app
CMD ["python", "inference.py"]