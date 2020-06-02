FROM node:12.7-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo


WORKDIR /project/app

COPY app/package.json app/package-lock.json ./

RUN set -ex \
  && npm install
