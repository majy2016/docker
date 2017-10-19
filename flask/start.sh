#!/bin/bash
# au majy<majiayang@zuozh.com>
nginx
gunicorn -w 4 -b 127.0.0.1:8000 transmit:app

while true
do
  sleep 1
done