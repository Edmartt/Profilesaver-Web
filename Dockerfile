FROM python:3.9.5-alpine

COPY requirements.txt .

RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apk del build-deps

COPY . .

CMD flask init-db ; flask run
