#!/bin/bash
# au majy<majiayang@zuozh.com>

if [ -e 'transmit.py' ] ;then
    service nginx start
    gunicorn -w 4 -b 127.0.0.1:8000 transmit:app
else
    tar xf pypj-1.0.tar.gz pypj-1.0/pypj --strip-components 2
    tar xf pypj-1.0.tar.gz pypj-1.0/setup.py  --strip-components 1
    mv setup.py ..
    cd ..
    python3 setup.py install
    service nginx start
    cd pypj
    gunicorn -w 4 -b 127.0.0.1:8000 transmit:app
fi
while true
do
  sleep 1
done