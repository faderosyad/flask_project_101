FROM ubuntu:20.04

MAINTAINER Fade Rosyad "faderosyad@gmail.com"

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install python3-dev python3-pip -y --fix-missing

COPY ./requirement.txt /app/requirement.txt

WORKDIR /app

RUN pip3 install Flask requests flask-mongoengine

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
