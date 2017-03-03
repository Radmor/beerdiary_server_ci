FROM python:3.5.2
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN pip install uwsgi

RUN mkdir /code
WORKDIR /code
ADD requirements/base.txt /code/
ADD requirements/dev.txt /code/
RUN pip install -r base.txt -r dev.txt --retries 500 --timeout 600
ADD . /code/

WORKDIR /code