# 🕷️ Black Widow 🕷️

## A stealthy TCP port scanner designed for network reconnaissance and security testing. 🔍🔒

### ✨ Overview ✨
**Black Widow** is a lightweight, highly configurable TCP port scanner written in Python. It leverages the power of Scapy for packet crafting and manipulation, allowing for stealthy network scanning operations. The tool is designed with security professionals and network administrators in mind, providing a simple yet effective way to identify open ports on target systems.

### 🚀 Features 🚀
* **🕵️ Stealth TCP SYN Scanning**: Performs half-open connections to detect open ports without completing the TCP handshake
* **🎯 Customizable Port Range**: Scan specific ports, port ranges, or comma-separated port lists
* **⚡ Multi-threaded**: Uses ThreadPoolExecutor for efficient concurrent scanning
* **📊 Clean Output**: Color-coded results for better readability
* **🔍 Verbose Mode**: Option to display open/filtered ports for comprehensive scanning

### 🔧 Installation 🔧

```bash
git clone https://github.com/CyLock11/Black-Widow.git
cd Black-Widow
chmod +x install.sh
sudo ./install.sh
```

### 📝 Usage 📝

```
./blackwidow.py [-h] -t TARGET [-p PORTS] [-v]
```

### 🔍 Arguments 🔍
* `-t TARGET`: IP address to scan (required) 🎯
* `-p PORTS`: Port range to scan (optional, default: 1-1000) 🔢
   * Single port: `-p 80`
   * Port range: `-p 1-1000`
   * Multiple ports: `-p 22,80,443`
   * All ports: `-p -`
* `-v`: Enable verbose mode to show open/filtered ports (optional) 🔊
* `-h, --help`: Show help message and exit ❓

### 💡 Examples 💡
Scan default ports on a target:

```bash
./blackwidow.py -t 192.168.1.1
```

Scan specific port range:

```bash
./blackwidow.py -t 192.168.1.1 -p 1-100
```

Scan specific ports:

```bash
./blackwidow.py -t 192.168.1.1 -p 22,80,443
```

Scan all ports:

```bash
./blackwidow.py -t 192.168.1.1 -p-
```

Enable verbose mode:

```bash
./blackwidow.py -t 192.168.1.1 -p 1-1000 -v
```

### 📚 Dependencies 📚
* Python 3.x 🐍
* Scapy 📦
* pwntools 🛠️
* termcolor 🎨
* concurrent.futures ⏱️

### 📁 Project Structure 📁

```
black_widow/
├── install.sh         # Installation script 🔧
├── blackwidow.py      # Main executable 🕷️
└── scan.py            # Core scanning functionality 🔍
```

### 🔄 Progress Tracking 🔄
The tool provides real-time feedback on scanning progress, displaying the number of active threads and notifying when the scan is complete.

### ⚠️ Disclaimer ⚠️
This tool is provided for educational and professional security testing purposes only. Users are responsible for ensuring they have proper authorization before scanning any networks or systems. 🔒
