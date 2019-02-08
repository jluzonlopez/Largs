FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y && apt-get install libnet-ifconfig-wrapper-perl -y && apt-get install iputils-ping -y && apt install python -y

COPY ./romanclient.py /tmp
COPY ./romanserver.py /tmp
COPY entrypoint.sh /

EXPOSE 12008
ENTRYPOINT ["/entrypoint.sh"]