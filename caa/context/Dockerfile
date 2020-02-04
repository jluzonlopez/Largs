FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y && apt-get install libnet-ifconfig-wrapper-perl -y && apt-get install iputils-ping -y && apt-get install ssh -y

COPY ./delta_hosts /tmp
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
