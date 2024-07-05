FROM ubuntu:latest
MAINTAINER Niema Moshiri <niemamoshiri@gmail.com>
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y g++ git make python3 python3-numpy python3-pandas python3-pip && \
    pip3 install --no-cache-dir --break-system-packages --force-reinstall setuptools==70.2.0 && \
    pip3 install --no-cache-dir --break-system-packages --force-reinstall setuptools-scm==8.0.4 && \
    pip3 install --no-cache-dir --break-system-packages --force-reinstall cython==0.29.37 && \
    pip3 install --no-cache-dir --break-system-packages --force-reinstall --no-binary :all: meson-python==0.16.0 ninja==1.11.1.1 nose==1.3.7 numpy==2.0.0 pandas==1.5.3 scikit-bio==0.6.1 wheel==0.43.0 && \
    pip3 install --no-cache-dir --break-system-packages --no-binary :all: bigtree biopython dendropy iow seaborn treeswift && \
    pip3 install --no-cache-dir --break-system-packages --no-binary :all: https://github.com/etetoolkit/ete/archive/ete4.zip && \
    rm -rf /root/.cache /tmp/*
