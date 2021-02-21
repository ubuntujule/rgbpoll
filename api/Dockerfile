FROM alpine:3.13

RUN apt-get install --no-cache --update \
            python3 \
            python3-pip

RUN pip3 install --upgrade --no-cache-dir \
        falcon \
        gunicorn \
#        falcon-cors \
#        requests
