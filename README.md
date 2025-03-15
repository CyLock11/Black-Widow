# Black-Widow - Stealth TCP Port Scanner

**Black-Widow** is a stealthy and efficient TCP port scanning tool designed to discover open ports on a target IP address quickly and with minimal network impact. It uses a stealth approach by sending SYN packets (half-open scan), allowing the scan to be conducted without fully establishing a connection.

## Features

- Stealthy TCP port scanning using SYN packets.
- Supports scanning ports in a range or specific ports provided by the user.
- Optimized scanning through multi-threading to improve speed.
- Informative output showing discovered ports in real-time.
- Simple command-line interface for specifying the target IP and ports to scan.

## Installation

To install **Black-Widow**, follow these steps:

1. Clone this repository or download the source code.
2. Run the installation script to set up the tool:

```bash
chmod +x install.sh
./install.sh
