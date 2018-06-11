#!/bin/bash
clear

echo "Update and install dependencies"
sudo apt-get update -y
sudo apt-get install -y python-pip python-serial python-requests build-essential python-dev git scons swig
pip install requests
echo " "

echo "Repo: fetch submodule"
git submodule init
git submodule update
cd rpi_ws281x
scons
cd python
sudo python setup.py install
cd ../..
echo " "

echo "Make script service start at boot"
sudo cp cheerlights.sh /etc/init.d/
sudo chmod 755 /etc/init.d/cheerlights.sh
sudo update-rc.d cheerlights.sh defaults
echo " "

echo "Run a script every minute to check if the processes needs respawned"
(sudo crontab -l ; echo "* * * * * /home/pi/repos/CheerlightsPi/autorestart.sh")| sudo crontab -
