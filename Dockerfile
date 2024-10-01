# Stage 1: Install dependencies
FROM python:3.8-slim AS builder
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Create a lightweight image with the app
FROM python:3.8-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
