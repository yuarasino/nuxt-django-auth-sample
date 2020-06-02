FROM python:3.8-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo


WORKDIR /project/api

COPY api/requirements*.txt api/constraints.txt ./

RUN set -ex \
  && python -m venv venv \
  && pip install -r requirements-dev.txt -c constraints.txt


ENV PYTHONDONTWRITEBYTECODE true
ENV PYTHONPATH /project/api/src
