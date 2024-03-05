FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apk add --no-cache mariadb-connector-c-dev build-base && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

CMD python main.py