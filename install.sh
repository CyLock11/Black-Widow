#!/bin/bash

pip3 install pwntools &>/dev/null
pip3 install scapy &>/dev/null
pip3 install termcolor &>/dev/null
pip3 install futures &>/dev/null

chmod +x scan.py blackwidow.py
mkdir -p /opt/black_widow
mv scan.py /opt/black_widow
mv blackwidow.py /usr/local/bin
