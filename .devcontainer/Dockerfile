FROM ubuntu:latest
MAINTAINER Niema Moshiri <niemamoshiri@gmail.com>
RUN apt-get update && apt-get -y upgrade && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y g++ git make python3 python3-numpy python3-pip && \
    pip3 install --no-cache-dir --break-system-packages bigtree biopython cython dendropy iow scikit-bio seaborn treeswift && \
    pip3 install --no-cache-dir --break-system-packages https://github.com/etetoolkit/ete/archive/ete4.zip && \
    rm -rf /root/.cache /tmp/*
