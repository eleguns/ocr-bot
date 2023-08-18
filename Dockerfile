FROM python:3.11-slim

COPY ./* /app/*

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

CMD ['python3', './src/main.py']
