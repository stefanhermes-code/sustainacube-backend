FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements_backend.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements_backend.txt

# Copy application code
COPY . .

# Create directory for CSV files
RUN mkdir -p /app/data

# Expose port
EXPOSE 8000

# Run the application
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}"]

