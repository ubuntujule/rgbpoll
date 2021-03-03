FROM alpine:3.13

#RUN apk update

RUN apk add --no-cache --update \
            python3 \
            py3-pip
 #        && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade --no-cache-dir \
        falcon \
        gunicorn
#        falcon-cors \
#        requests
COPY api.py .
CMD ["gunicorn", "/api:app", "--bind", "0:80"]
