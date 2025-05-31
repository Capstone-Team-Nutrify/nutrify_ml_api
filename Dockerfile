FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Copy dependency file dan install dulu
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code
COPY . ./

# Tentukan port (opsional, hanya dokumentasi)
EXPOSE 8080

# Jalankan aplikasi
CMD ["python", "main.py"]
