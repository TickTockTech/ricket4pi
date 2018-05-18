#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

PROJ_DIR="$( cd "$(dirname "$0")/../" ; pwd -P )"
echo "Project directory: " $PROJ_DIR

apt-get update
apt-get install supervisor

pip install websocket-server

cp $PROJ_DIR/scripts/ricket_www.conf /etc/supervisor/conf.d/
cp $PROJ_DIR/scripts/ricket_websock.conf /etc/supervisor/conf.d/

# sed 's/old/new/' input.txt
sed -i "s@\[install_dir\]@$PROJ_DIR@g" /etc/supervisor/conf.d/ricket_www.conf
sed -i "s@\[install_dir\]@$PROJ_DIR@g" /etc/supervisor/conf.d/ricket_websock.conf

supervisorctl update
