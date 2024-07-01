FROM ubuntu:latest
MAINTAINER Niema Moshiri <niemamoshiri@gmail.com>
RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y g++ git make python3 python3-pip && \
    pip3 install --no-cache-dir dendropy treeswift && \
    pip3 install --no-cache-dir https://github.com/etetoolkit/ete/archive/ete4.zip && \
    rm -rf /root/.cache /tmp/*
