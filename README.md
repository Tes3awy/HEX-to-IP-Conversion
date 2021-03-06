[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg?logo=python&style=flat-square)](https://www.python.org/downloads)
[![Code Size](https://img.shields.io/github/languages/code-size/Tes3awy/HEX-to-IP-Conversion?color=green&style=flat-square)](https://github.com/Tes3awy/HEX-to-IP-Conversion)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square)](https://github.com/pre-commit/pre-commit)
[![License](https://img.shields.io/github/license/Tes3awy/HEX-to-IP-Conversion?color=purple&style=flat-square)](https://github.com/Tes3awy/HEX-to-IP-Conversion)

# Convert IPv4 Address to Hexadecimal Address and vice versa

> This application is useful for Cisco Wireless and Collaboration teams where Hexadecimal Addresses are preferably to be used in DHCP pools option commands.

**DHCP Pools Example**

```powershell
configure terminal
!
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
   lease 86400
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
│   conversion.py  # conversion class
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
path\to\folder> git clone https://github.com/Tes3awy/HEX-to-IP-Conversion.git
path\to\folder> cd HEX-to-IP-Conversion
path\to\folder> py -m venv .venv
path\to\folder> .venv\Scripts\Activate.ps1
path\to\folder> py -m pip install --upgrade pip setuptools
path\to\folder> py -m pip install -r requirements.txt
```

### Installation on macOS and Linux

```bash
$ git clone https://github.com/Tes3awy/HEX-to-IP-Conversion.git
$ cd HEX-to-IP-Conversion
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python3 -m pip install --upgrade pip setuptools
$ python3 -m pip install -r requirements.txt --upgrade
```

---

### Usage

```bash
(.venv)$ python -m main

[1] IPv4 to Hex
[2] Hex to IPv4

Enter 1 or 2 [Default 1]:

```
