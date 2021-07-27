FROM ubuntu:20.04

ENV LANG en_US.utf8

ENV TZ = "America/Bogota"

RUN yes | apt-get update

RUN  yes | DEBIAN_FRONTEND="noninteractive" apt-get install python3.9