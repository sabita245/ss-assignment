# Use Python 3.9 as base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn

# Set working directory
WORKDIR /app

# Copy application code into the container
COPY ./app /app

# Expose the port on which the app will run
EXPOSE 8000

# Run the app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

