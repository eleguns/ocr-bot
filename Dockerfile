FROM ubuntu:latest

RUN apt install python3.11-dev python3.11-pip

COPY ./* /app/*

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

CMD ['python3', './src/main.py']
