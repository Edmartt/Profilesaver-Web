FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV FLASK_RUN_HOST 0.0.0.0

CMD flask init-db ; flask run
