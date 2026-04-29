# Building Stage
FROM python:3.12-slim as builder

LABEL author="Fade Rosyad"
LABEL email="faderosyad@gmail.com"

WORKDIR /build
COPY . .

RUN apt-get update && apt-get install -y binutils
RUN pip3 install -r requirement.txt

# this experiment with multibuild python is kinda useless
#RUN pyinstaller --onefile app.py --add-data "templates:templates" --name flaskweb

# Deliver the Image
#FROM debian:bookworm-slim as delivery

#WORKDIR /app

#COPY --from=builder /build/dist/flaskweb .

#RUN chmod +x flaskweb

ENTRYPOINT [ "python3", "app.py" ]
