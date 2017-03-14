FROM python:3.5.2
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN pip install uwsgi

RUN mkdir /code
WORKDIR /code
ADD requirements /code/
RUN pip install -r base.txt -r dev.txt -r test.txt
ADD . /code/

WORKDIR /code