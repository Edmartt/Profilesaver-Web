FROM python:3.7-alpine3.13

WORKDIR /app

COPY . /app

RUN apk update \
	&& apk add --virtual build-deps gcc python3-dev musl-dev\
	&& apk add --no-cache mariadb-dev

RUN pip install -r requirements.txt
RUN apk del build-deps

ENV FLASK_RUN_HOST 0.0.0.0

CMD flask init-db ; flask run
