# Ricket4Pi

Python code for 4tronix initio robot buggy. Web-Interface to make it more accessible using a tablet, laptop, phone, etc...

# To Install from Package on the Buggy

    sudo apt-get update
    sudo apt-get install supervisor
    sudo pip install git+https://github.com/Pithikos/python-websocket-server
    wget https://github.com/ticktocktech/ricket4pi/raw/master/builds/ricket4pi_0.0-3_all.deb
    sudo dpkg -i ricket4pi_0.0-3_all.deb


# Install

    git clone https://github.com/ticktocktech/ricket4pi.git
    cd ricket4pi
    cd bin
    ./install.sh

# To Operate Buggy

    Switch on Raspberry Pi mounted on 4Tronix Initio buggy.
    Open 'http://[Initio Raspberry Pi IP address]:8080' in a browser on another machine or tablet.
    Control buggy with buttons on web-page.
   

# Running Server on Raspberry Pi

To Start:

    sudo supervisorctl start ricket:websock
    sudo supervisorctl start ricket:www

or

    sudo supervisorctl start ricket:*

To Stop:
    
    sudo supervisorctl stop ricket:www
    sudo supervisorctl stop ricket:websock

or

    sudo supervisorctl stop ricket:*
   
To Check:

    sudo supervisorctl status


# Notes

Web Sockets provided by:

https://github.com/Pithikos/python-websocket-server

Robohat python code downloaded from:

http://4tronix.co.uk/robohat/robohat.py

Wheel sensor code originally cloned from:

https://github.com/ailiev/robohat
