FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y && apt-get install libnet-ifconfig-wrapper-perl -y && apt-get install iputils-ping -y && apt-get install ssh -y && apt-get install openssh-server -y
RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginiud.so@g' -i /etc/pam.d/sshd
COPY ./delta_hosts /tmp
COPY entrypoint.sh /

EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
