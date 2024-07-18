# Start your image with a node base image
FROM python:3.10-slim-buster
EXPOSE 8000

# The /app directory should act as the main application directory
WORKDIR /app

RUN apt-get update && apt-get install -y vim nano


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./server .

ENV TZ=Asia/Seoul

ENTRYPOINT python server.py
