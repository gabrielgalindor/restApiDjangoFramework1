FROM ubuntu:20.04

ENV LANG en_US.utf8

ENV TZ = "America/Bogota"

RUN yes | apt-get update

RUN  yes | DEBIAN_FRONTEND="noninteractive" apt-get install python3.9

RUN apt update

RUN yes | apt install python3-pip

RUN pip install django

RUN pip install djangorestframework==3.12.4

RUN pip install PyMySQL==1.0.2

RUN yes | apt install git

RUN apt update

RUN cd var

RUN git clone https://ggalindo-acreditta:dXJMVRZqLNtwY978@github.com/gabrielgalindor/restApiDjangoFramework1.git

RUN yes | apt-get install mysql-server