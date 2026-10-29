FROM python:3.9-slim

# تثبيت أداة ffmpeg والنظام الأساسي للبث
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY stream.py .

CMD ["python", "stream.py"]
