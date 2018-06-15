#!/bin/bash
clear

echo "Update and install dependencies"
sudo apt-get update -y
sudo apt-get install -y vim python3-pip python-serial python-requests build-essential python-dev git scons swig -y

sudo apt install python3-pip python3-venv -y 
python3 -m venv env 
source env/bin/activate 
pip3 install -r requirements.txt 
python -V
echo " "

echo "Repo: fetch submodule"
git submodule init
git submodule update
cd rpi_ws281x
# vi main.c
scons
cd python
python ./setup.py build
sudo python ./setup.py install
cd ..
sudo ./test -c
cd ..
echo " "

#echo "Make script service start at boot"
#sudo cp cheerlights.sh /etc/init.d/
#sudo chmod 755 /etc/init.d/cheerlights.sh
#sudo update-rc.d cheerlights.sh defaults
#echo " "

#echo "Run a script every minute to check if the processes needs respawned"
#(sudo crontab -l ; echo "* * * * * /home/pi/repos/CheerlightsPi/autorestart.sh")| sudo crontab -
