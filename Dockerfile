FROM python:3.7-alpine

ENV ENVIRONMENT_DATABASE=iweb \
ENVIRONMENT_USER=DiP \
ENVIRONMENT_PASSWORD=DiP2019 \
ENVIRONMENT_PORT=5432 \
ENVIRONMENT_HOST=postgre \
PYTHONPATH=/api \
ENVIRONMENT_PRODUCTION=True

RUN mkdir /api
COPY . /api
WORKDIR /api

RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev && \
    pip install -r requirements.txt && \
    pip install  gunicorn gunicorn[gevent] gevent && \
    apk --purge del .build-deps && \
    apk add --no-cache postgresql-libs jpeg zlib freetype lcms2 openjpeg tiff tk tcl binutils libc-dev

EXPOSE 4000

CMD gunicorn BiceaterBackend.wsgi -c gunicornConfig.py