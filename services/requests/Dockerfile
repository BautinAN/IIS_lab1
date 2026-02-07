FROM python:3.11-slim

WORKDIR /requests_service

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY requests_docker.py .

CMD ["python", "requests_docker.py"]

# Команда сборки образа
# docker build -t requests_service:1 .

# Команда запуска контейнера
# docker run --name requests_service_container --rm requests_service:1