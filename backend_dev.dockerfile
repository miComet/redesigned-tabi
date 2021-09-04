FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y apt-utils && \
    apt-get install -y tmux git vim python3 python3-pip

RUN pip3 install --upgrade pip setuptools

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV LANG C.UTF-8
ENV LC_ALL=C.UTF-8

WORKDIR /project

CMD /project/scripts/launch_backend.sh
