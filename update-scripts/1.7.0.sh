#!/bin/bash

sudo pip3 install open-cravat -U
logDir=/usr/local/lib/python3.6/site-packages/cravat/logs
sudo mkdir -p $logDir
log=$logDir/wcravat.log
sudo touch $log
sudo chmod a+rw $log
sudo env "PATH=$PATH" oc config md /mnt/ssd/oc
sudo chown centos:centos /mnt/ssd/oc/* -R
oc module update -y
sudo shutdown now