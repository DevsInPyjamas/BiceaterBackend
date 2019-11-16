FROM python:3.7-alpine

ENV DB_NAME=iweb \
DB_USER=DiP \
DB_PASSWORD=DiP2019 \
DB_PORT=5432 \
DB_HOST='192.168.1.20'

RUN mkdir /api
COPY . /api
WORKDIR /api

RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev && \
    pip install -r requirements.txt && \
    pip install  gunicorn gunicorn[gevent] gevent && \
    apk add --no-cache postgresql-libs jpeg zlib freetype lcms2 openjpeg tiff tk tcl binutils libc-dev && \
    apk --purge del .build-deps

CMD gunicorn -k gevent BiciterBackend.wsgi -b 0.0.0.0:4000