#!/bin/bash
clear
echo "

┏┓┏━┳━━┳┓┏━┳┓╋┏┓
┃┃┃┏┻┫┣┫┃┃┏┫┃╋┃┃
┃┗┛┛╋┃┃┃┗┛┛┃┃╋┃┃
┃┏┓┃╋┃┃┃┏┓┃┃┃╋┃┃
┃┃┃┗┳┫┣┫┃┃┗┫┗━┛┃
┗┛┗━┻━━┻┛┗━┻━━━┛
                              

"
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/kikubots/kiku/master/kiku-setup.py
pip install telethon
python kiku-setup.py
