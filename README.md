[![Tested on Python 3.6+](https://img.shields.io/badge/python-3.6+-yellow.svg?logo=python)](https://www.python.org/downloads)
[![Code Size](https://img.shields.io/github/languages/code-size/Tes3awy/HEX-to-IP-Conversion?color=green)](https://github.com/Tes3awy/HEX-to-IP-Conversion)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![License](https://img.shields.io/github/license/Tes3awy/HEX-to-IP-Conversion?color=purple)](https://github.com/Tes3awy/HEX-to-IP-Conversion)

# Convert IPv4 Address to HEX IP and vice versa

This application is designed to convert an IPv4 Address to a HEX IP and vice versa.

> This aplication is useful for Cisco Wireless and Collaboration teams where HEX IPs are preferably to be used in DHCP pools options.

**DHCP Pools Example**

```powershell
ip dhcp pool APs
   network 60.0.0.0 255.255.255.0
   default-router 60.0.0.1
   option 43 hex f104.0a0a.0a0f
exit
!
ip dhcp pool Voice
   network 192.168.1.0 255.255.255.0
   default-router 192.168.1.1
   option 150 hex c0a8.0101
exit
!
end
```

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation on Windows](#installation-on-windows)
3. [Installation on macOs and Linux](#installation-on-macos-and-linux)
4. [Usage](#usage)

### Getting Started

**Directory Structure**

```bash
│   main.py  # Main application
│   ip_to_hex.py  # IPv4 Address to HEX IP function
│   hex_to_ip.py  # HEX IP to IPv4 Address function
│   README.md
│   requirements.txt
│   .pre-commit-config.yaml
│   .gitignore
│   LICENSE
└───
```

---

### Installation on Windows

```bash
$ git clone https://github.com/Tes3awy/HEX-to-IP-Conversion.git
$ cd HEX-to-IP-Conversion
$ py -m venv .venv
$ py -m pip install -r requirements.txt --user --upgrade
```

### Installation on macOS and Linux

```bash
$ git clone https://github.com/Tes3awy/HEX-to-IP-Conversion.git
$ cd HEX-to-IP-Conversion
$ python3 -m venv .venv
$ python3 -m pip install -r requirements.txt --user --upgrade
```

---

### Usage

**Windows**

```powershell
> cd ./venv/Scripts/Activate.ps1
(.venv)> py main.py
```

**macOS and \*nix**

```bash
$ source .venv/bin/activate
(.venv)$ python3 main.py
```
