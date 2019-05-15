# CyWoodsHackathon
```
#this is a test

#!/bin/bash
echo "Setting up SSH"
ssh-keygen -t rsa
echo "Installing dependencies"
apt-get install python3-pip git vim woof npm tmux
#spooky fucking microsoft ppa stuff
echo "spooky microsoft stuff to download vscode"
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install code
echo "installing django stuff"
pip3 install django djangorestframework django-cors-headers
echo "installing npm stuff / react stuff"
npm install -g create-react-app
apt remove cmdtest
npm install -g yarn
npm install -g react-scripts
echo 'run these commands to set up git'
echo 'git config --global user.email "you@example.com"'
echo 'git config --global user.name "Your Name"'
```
Hello World!

