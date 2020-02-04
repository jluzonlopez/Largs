#!/bin/bash
cat /tmp/delta_hosts >> /etc/hosts
mkdir /home/juan/.ssh
cp /tmp/id_ed25519.pub /home/juan/.ssh/authorized_keys
chmod 700 /home/juan/.ssh
chmod 600 /home/juan/.ssh/*
chown juan /home/juan
chown juan /home/juan/.ssh
chown juan /home/juan/.ssh/*
chgrp juan /home/juan
chgrp juan /home/juan/.ssh
chgrp juan /home/juan/.ssh/*
echo "IdentifyFile ~/.ssh/id_ed25519" >> /etc/ssh/ssh_config
/usr/sbin/sshd
/bin/bash
