FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instalar curl
RUN apt-get update && apt-get install -y curl

COPY . .

CMD ["python", "app.py"]
