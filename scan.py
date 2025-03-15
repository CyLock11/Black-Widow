#!/usr/bin/env python3

from pwn import log
from termcolor import colored
from scapy.all import *


class TCPScan:

    def __init__(self, target):

        self.target = target

    def scan_port(self, port):

        pkt = IP(dst=self.target) / TCP(dport=port, flags="S")

        response = sr1(pkt, timeout=3, verbose=0)

        if response.getlayer(TCP).flags == 0x012:

            log.info(colored(f"Discovered open port {port}/tcp on {self.target}"))

    def show_info(self):

        pass
