#!/bin/bash
cat /tmp/delta_hosts >> /etc/hosts
mkdir /root/.ssh
cp /tmp/id_ed25519 /root/.ssh/id_ed25519
chmod 700 /root/.ssh
chmod 600 /root/.ssh/*
/bin/bash
