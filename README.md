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

---

### 📫 Contact & Socials

<p align="center">
  <a href="mailto:aryanbhalsing7090@gmail.com">
    <img src="https://img.shields.io/badge/Email-aryanbhalsing7090%40gmail.com-red?style=for-the-badge&logo=gmail" />
  </a>
  <a href="https://www.linkedin.com/in/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/LinkedIn-iamaryanbhalsing-blue?style=for-the-badge&logo=linkedin" />
  </a>
  <a href="https://github.com/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/GitHub-iamaryanbhalsing-black?style=for-the-badge&logo=github" />
  </a>
  <a href="https://leetcode.com/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/LeetCode-Profile-orange?style=for-the-badge&logo=leetcode" />
  </a>
</p>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=iamaryanbhalsing&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views" />
</p>

---
<img src="https://camo.githubusercontent.com/a5dbb660f658cb0ba61949a83a2eac3bde636395a476ecc7c16124d2a1f9d8a0/68747470733a2f2f73746174732e70706861742e746f702f69636f6e733f6e616d653d6170706c652c617263686c696e75782c646f636b65722c646a616e676f2c666173746170692c6769746c61622c6769742c6769746875622c6a736f6e2c6a6176617363726970742c6c696e75782c6d6f6e676f64622c6e656f76696d2c6e67696e782c706f737467726573716c2c707974686f6e2c727573742c72656163742c72656469732c7461696c77696e646373732c26636f6c756d6e733d3230" />

---
