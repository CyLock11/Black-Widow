# Black Widow

A stealthy TCP port scanner designed for network reconnaissance and security testing.

## Overview

Black Widow is a lightweight, highly configurable TCP port scanner written in Python. It leverages the power of Scapy for packet crafting and manipulation, allowing for stealthy network scanning operations. The tool is designed with security professionals and network administrators in mind, providing a simple yet effective way to identify open ports on target systems.

## Features

- **Stealth TCP SYN Scanning**: Performs half-open connections to detect open ports without completing the TCP handshake
- **Customizable Port Range**: Scan specific ports, port ranges, or comma-separated port lists
- **Multi-threaded**: Configurable thread count for faster scanning
- **Clean Output**: Color-coded results for better readability
- **Easy Installation**: Simple bash script to install all dependencies

## Installation

```bash
git clone https://github.com/yourusername/black-widow.git
cd black-widow
chmod +x install.sh
sudo ./install.sh
```

## Usage

```
blackwidow.py [-h] -t TARGET [-p PORTS] [--threads THREADS]
```

### Arguments

- `-t TARGET`: IP address to scan (required)
- `-p PORTS`: Port range to scan (optional, default: 1-1000)
  - Single port: `-p 80`
  - Port range: `-p 1-1000`
  - Multiple ports: `-p 22,80,443`
- `--threads THREADS`: Maximum number of threads (optional, default: 20)
- `-h, --help`: Show help message and exit

### Examples

Scan default ports on a target:
```bash
blackwidow.py -t 192.168.1.1
```

Scan specific port range:
```bash
blackwidow.py -t 192.168.1.1 -p 1-100
```

Scan specific ports:
```bash
blackwidow.py -t 192.168.1.1 -p 22,80,443
```

Scan with 40 threads:
```bash
blackwidow.py -t 192.168.1.1 -p 1-1000 --threads 40
```

## Dependencies

- Python 3.x
- Scapy
- pwntools
- termcolor
- concurrent.futures

## Project Structure

```
black-widow/
├── install.sh         # Installation script
├── blackwidow.py      # Main executable
└── scan.py            # Core scanning functionality
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is provided for educational and professional security testing purposes only. Users are responsible for ensuring they have proper authorization before scanning any networks or systems.
