FROM python:3-slim

RUN apt-get update && \
    apt-get install -y python3-pip && \
    python3 -m pip install Django && \
    rm -rf /var/lib/apt/lists/*

COPY . /rgbpoll

RUN pip3 install -r /rgbpoll/requirements.txt

WORKDIR rgbpoll

CMD ./manage.py runserver 0:8010
