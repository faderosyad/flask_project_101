FROM ubuntu:18.04

MAINTAINER Fade Rosyad "faderosyad@gmail.com"

RUN apt-get update -y && apt-get upgrade -y && apt-get install python python3 python-pip python3-pip -y

COPY ./requirement.txt /app/requirement.txt

WORKDIR /app

RUN pip install -r requirement.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
