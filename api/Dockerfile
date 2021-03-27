FROM alpine:3.13

#RUN apk update

RUN apk add --no-cache --update \
            python3 \
            py3-pip
 #        && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade --no-cache-dir \
        falcon \
        gunicorn3
#        falcon-cors \

#        requests
CMD gunicorn app:api -b 0:8000
