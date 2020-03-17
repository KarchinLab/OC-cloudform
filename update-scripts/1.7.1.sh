#!/bin/bash

sudo pip3 install open-cravat -U
sudo chown centos:centos /mnt/ssd/oc/* -R
oc module update -y
sudo sed -i '/max_num_concurrent_annotators_per_job/d' /usr/local/lib/python3.6/site-packages/cravat/conf/cravat-system.yml

# Cleanup
sudo shred -u /etc/ssh/*_key /etc/ssh/*_key.pub
shred -u ~/.*history

# Shutdown
sudo shutdown now
