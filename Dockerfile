FROM python:3.7

WORKDIR /app

RUN apt-get update -y && \ 
    apt-get install gcc

RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 5000

CMD ["flask init-db; flask run"]
