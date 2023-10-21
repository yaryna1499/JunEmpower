FROM python:3.11-alpine

WORKDIR /app

COPY . /app
# встановлення bash в контейнері
RUN apk add --no-cache bash
# встановлення утиліти nc щоб ранити команди для Postgres
RUN apk add --no-cache netcat-openbsd

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

ENTRYPOINT "./docker/python/entrypoint.sh"
