#! /bin/bash

sudo cp py_svc1.service /lib/systemd/system/
sudo cp py_svc2.service /lib/systemd/system/

sudo systemctl daemon-reload

sudo systemctl restart py_svc1.service
sudo systemctl restart py_svc2.service

tail -f /var/log/syslog