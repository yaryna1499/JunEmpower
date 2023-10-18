FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

ENTRYPOINT "./docker/python/entrypoint.sh"
