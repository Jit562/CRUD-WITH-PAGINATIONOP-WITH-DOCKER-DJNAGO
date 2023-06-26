FROM python:3.11-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /doct
COPY requirements.txt /doct/
RUN apt-get update
RUN pip install -r requirements.txt
COPY ./doct/ /doct/