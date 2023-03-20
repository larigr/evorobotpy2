FROM python:3.10-alpine

WORKDIR /usr/app/src

COPY . .

RUN pip install -r requirements.txt

RUN make compile_all



