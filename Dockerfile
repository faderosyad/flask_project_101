# Building Stage
FROM python:3.12-alpine as builder

LABEL author="Fade Rosyad"
LABEL email="faderosyad@gmail.com"

WORKDIR /build
COPY . /build

RUN apk add binutils
RUN pip3 install -r requirement.txt

RUN pyinstaller --onefile app.py --add-data "templates:templates" --name flaskweb

# Deliver the Image
FROM gcr.io/distroless/python3-debian13 as delivery

WORKDIR /app

COPY --from=builder /build/dist/flaskweb .

ENTRYPOINT [ "./flaskweb" ]
