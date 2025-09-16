FROM python:3.11-slim

RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY server.py /app
RUN pip install flask

CMD ["python", "server.py"]
