FROM python:3.12-alpine

LABEL author="Fade Rosyad"
LABEL email="faderosyad@gmail.com"

COPY ./requirement.txt /app/requirement.txt

WORKDIR /app

RUN pip3 install Flask requests flask-mongoengine

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
