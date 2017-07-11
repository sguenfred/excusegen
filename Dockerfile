FROM registry-os.prod.vdc.p.fti.net:443/hebex/ubuntu:16.04
MAINTAINER fbenoit.ext@orange.com

# Preconisations VDC
ENV DEBIAN_FRONTEND noninteractive
ENV INITRD no
RUN dpkg-divert --local --rename --add /usr/bin/ischroot
RUN ln -sf /bin/true /usr/bin/ischroot
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# Installation des paquets
RUN echo "deb http://master-repo-build01.install-os.s1.p.fti.net/dfy xenial-dev vdc" >/etc/apt/sources.list.d/dfy_xenial_dev_vdc.list
RUN apt-get -y update && apt-get install -y python python-dev \
    && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Copie de fichiers
COPY generate.py /root/

#Start
WORKDIR /
CMD python /root/generate.py
