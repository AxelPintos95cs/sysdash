FROM python:3.10-slim

RUN apt-get update && apt-get install -y gcc
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY main.py .         
COPY tests /app/tests  

CMD ["python", "main.py"]
