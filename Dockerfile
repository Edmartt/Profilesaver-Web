FROM python:3.7

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update && apt-get install gcc musl-dev

RUN pip install -r requirements.txt

COPY . .
