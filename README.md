# Port Scanner

A simple, fast, and user-friendly **TCP Port Scanner** written in Python.

---
## Features

- Scan any IP address or hostname
- Customizable port range
- Multi-threaded scanning (fast performance)
- Service name detection (e.g., ssh, http, https)
- Supports both **interactive** and **command-line** usage
- Clean, readable output

---
## Installation

No external dependencies required. Just Python 3.

```bash
# Clone or download the project
git clone https://github.com/iamaryanbhalsing/port-scanner
cd port-scanner
```

```
Usage
1. Interactive Mode
Bashpython3 port_scanner.py
2. Command Line Mode
Bash# Scan localhost with default range (1-100)
python3 port_scanner.py 127.0.0.1

# Custom port range
python3 port_scanner.py 192.168.1.1 -s 1 -e 500

# Scan a specific range on a domain
python3 port_scanner.py example.com --start 80 --end 443
Command Line Arguments
```

---

## Project Structure
```
port-scanner/
├── port_scanner.py     # Main scanner program
├── README.md           # Documentation (this file)
└── scans/              # (Optional) Folder to save scan results
```

---

## Example Output
```
Scanning 127.0.0.1 from port 1 to 100...

✅ Open ports found:
   Port 22    → ssh
   Port 80    → http
   Port 443   → https
```

---

## Legal & Safety Notice
⚠️ Important: Only use this tool on systems you own or have explicit permission to scan. Unauthorized port scanning may be illegal in your jurisdiction.

---
