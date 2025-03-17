#!/usr/bin/env python3

from pwn import log
from termcolor import colored
from scapy.all import *


class TCPScan:

    def __init__(self, target):

        self.target = target
        self.discovered_ports = []

    def scan_port(self, port_plus_verbose):

        port = port_plus_verbose[0]
        verbose = port_plus_verbose[1]

        pkt = IP(dst=self.target) / TCP(dport=port, flags="S")

        response = sr1(pkt, timeout=3, verbose=0)

        if not response is None:

            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x012:

                log.info(colored(f"Discovered open port {port}/tcp on {self.target}", 'blue'))
                self.discovered_ports.append(port)

                rst_pkt = IP(dst=self.target) / TCP(dport=port, flags="R")
                send(rst_pkt, verbose=0)

        elif verbose:

            log.warning(colored(f"Discovered open/filtered port {port}/tcp on {self.target}", 'yellow'))

    def show_info(self):

        if self.discovered_ports:

            print(); log.success(colored(f"Discovered Ports: {','.join(map(str, sorted(self.discovered_ports)))}", 'green'))

        else:

            log.failure(colored("Discovered Ports: there aren't discovered ports", 'red'))
