FROM python:3.10-slim

COPY . /app/

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libportaudio2 \
    portaudio19-dev \
    gcc \
    libc-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["python","app.py"]