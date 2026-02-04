FROM python:3.11-slim

WORKDIR /ml_service

RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OMP_NUM_THREADS=1

VOLUME /models

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Команда для сборки образа:
# docker build -t ml_service:1 .

# Команда для запуска контейнера:
# docker run -d   -p 8000:8000   -e OMP_NUM_THREADS=1   -e MKL_NUM_THREADS=1   -v $(pwd)/../models:/models   --name ml_service_container ml_service:1