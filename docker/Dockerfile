FROM ubuntu:20.04
ENV PYTHONBUFFERED 1
RUN apt-get update -y &&\
    apt-get install -y python3.8 python3-pip git &&\
    pip install pandas

WORKDIR /app
COPY src/ /app/src/
COPY data/ /app/data/
