FROM ubuntu:latest

WORKDIR /home/

RUN apt-get update && apt-get install -y python python3 virtualenv
RUN virtualenv -p python3 wayoming
