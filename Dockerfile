FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
RUN [ "$INSTALL_DEV" = "true" ] && pip install --no-cache-dir -r requirements-dev.txt || true
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]