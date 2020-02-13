#!/bin/bash

sudo pip3 install open-cravat -U
sudo sed -i 's/\r$//g' /usr/local/lib/python3.6/site-packages/cravat/cravat_web.py
sudo patch /usr/local/lib/python3.6/site-packages/cravat/cravat_web.py <<EOF
46,49d45
<     log_handler = logging.handlers.TimedRotatingFileHandler(log_path, when='d', backupCount=30)
<     log_formatter = logging.Formatter('%(asctime)s: %(message)s', '%Y/%m/%d %H:%M:%S')
<     log_handler.setFormatter(log_formatter)
<     logger.addHandler(log_handler)
166a163,166
>     log_handler = logging.handlers.TimedRotatingFileHandler(log_path, when='d', backupCount=30)
>     log_formatter = logging.Formatter('%(asctime)s: %(message)s', '%Y/%m/%d %H:%M:%S')
>     log_handler.setFormatter(log_formatter)
>     logger.addHandler(log_handler)
EOF
sudo env "PATH=$PATH" oc config md /mnt/ssd/oc
sudo chown centos:centos /mnt/ssd/oc/* -R
oc module update -y
sudo shutdown now