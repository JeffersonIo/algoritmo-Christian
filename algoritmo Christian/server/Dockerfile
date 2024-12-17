FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip  # Actualiza pip
RUN pip install --no-cache-dir -r requirements.txt

COPY time_server.py .

EXPOSE 5000

CMD ["python", "time_server.py"]
