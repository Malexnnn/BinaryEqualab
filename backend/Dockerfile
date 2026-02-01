
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file from backend directory explicitly
# Assumes Docker Build Context is set to "." (Repo Root)
COPY backend/requirements.txt .

# Install dependencies (no PyQt6 here)
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code into /app
COPY backend/ .

# Copy shared src directory into /app/src
COPY src/ ./src

# Make port 8000 available
EXPOSE 8000

# Define environment variables
ENV PORT=8000
ENV PYTHONPATH=/app

# Run app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
