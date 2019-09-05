FROM        accent/starlette-docker:3.7-alpine

RUN         set -ex \
           && apk update \
           && apk add --no-cache \
           build-base python-dev openblas-dev freetype-dev pkgconfig gfortran \
    	   && ln -s /usr/include/locale.h /usr/include/xlocale.h \
           && pip install --upgrade pip \
           && pip install --no-cache \
	   numpy \
           matplotlib \
           scipy \
           scikit-learn \
           pandas \
           nltk \
           && apk del build-runtime \
           && apk add --no-cache --virtual build-dependencies \
	   dumb-init \
    	   musl \
    	   libc6-compat \
    	   linux-headers \
    	   build-base \
    	   bash \
    	   git \
    	   ca-certificates \
    	   freetype \
    	   libgfortran \
    	   libgcc \
    	   libstdc++ \
    	   openblas \
    	   tcl \
    	   tk \
    	   libssl1.0 \
           && rm -rf /var/cache/apk/*

ARG         REQUIREMENTS_FILE=/requirements/base.txt

ENV         APP_MODULE=app.main:app \
            ALLOWED_HOSTS="*" \
            DATABASE_URL=postgresql+psycopg2://postgres:password@db:5432/appdb \
            SECRET_KEY="***** change me *****" \
            EMAIL_HOST=mail \
            EMAIL_PORT=1025 \
            EMAIL_DEFAULT_FROM_ADDRESS=mail@example.com \
            EMAIL_DEFAULT_FROM_NAME=Mail
