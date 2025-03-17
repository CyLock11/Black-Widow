#!/usr/bin/env python3

import sys
sys.path.append("/opt/black_widow/")

# Custom class
from scan import TCPScan

from pwn import *
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored
import signal, argparse, re, os, subprocess

# Salto de línea
print()

def def_handler(sig, frame):

    print(colored("\n\n[-] Saliendo...", 'red'))
    subprocess.run(["tput", "cnorm"])
    os._exit(0)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

def filter_args(target, ports):

    regex_target = r'^([0-9]{1,3}\.){3}([0-9]{1,3})$'

    match_target = re.match(regex_target, target)

    if ports == '-':

        regex_ports = r'^\-$'
        port_type = "all"

    elif '-' in ports:

        regex_ports = r'^([0-9]{1,5})\-([0-9]{1,5})$'
        port_type = "g"

    elif ',' in ports:

        regex_ports = r'^([0-9]{1,5}){1}(\,[0-9]{1,5}){1,}$'
        port_type = "c"

    else:

        regex_ports = r'^([0-9]{1,5})$'
        port_type = "a"

    match_ports = re.match(regex_ports, ports)

    if match_target and match_ports:

        return True, port_type

    else:

        return False, None

def parse_ports(ports, port_type):

    if port_type == 'all':

        return range(1, 65536)

    elif port_type == 'g':

        split_ports = ports.split('-')
        filter_ports = tuple([port for port in range(int(split_ports[0]), int(split_ports[1]) + 1)])

        return filter_ports

    elif port_type == 'c':

        filter_ports = tuple([int(port) for port in ports.split(',')])

        return filter_ports

    elif port_type == 'a':

        return (int(ports),)

def get_arguments():

    parser = argparse.ArgumentParser(description="Stealth TCP Port Scanner")
    parser.add_argument('-t', required=True, dest='target', help='IP Address to Scan')
    parser.add_argument('-p', required=False, dest='ports', help='Port Range (default: 1-1000)')
    parser.add_argument('-v', required=False, action="store_true", help="Print Filtered Ports (default: False)")

    args = parser.parse_args()

    if '-h' in sys.argv or '--help' in sys.argv:

        parser.print_help()
        subprocess.run(["tput", "cnorm"])
        sys.exit(0)

    if args.ports is None:

        args.ports = "1-1000"

    is_valid, port_type = filter_args(args.target, args.ports)

    if is_valid:

        args.ports = parse_ports(args.ports, port_type)

        try:

            return args.target, args.ports, args.v

        except:

            subprocess.run(["tput", "cnorm"])
            sys.exit(colored("\n[-] Syntax Error: Threads are not valid", 'red'))

    else:

        subprocess.run(["tput", "cnorm"])
        sys.exit(colored("\n[-] Syntax Error: IP or Ports are not valid", 'red'))

if __name__ == '__main__':

    target, ports, verbose = get_arguments()

    scanner = TCPScan(target)

    p1 = log.progress("Active threads")
    count = 0

    subprocess.run(["tput", "civis"])
    
    with ThreadPoolExecutor(max_workers=20) as executor:

        futures = []

        for port in ports:

            count += 1
            p1.status(f"{count}\n\n")
            futures.append(executor.submit(scanner.scan_port, (port, verbose)))

        for future in futures:

            future.result()

    p1.success("Scan completed!")

    scanner.show_info()

    # Devolver cursor
    subprocess.run(["tput", "cnorm"])
