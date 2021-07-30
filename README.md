[![Tested on Python 3.6+](https://img.shields.io/badge/%20-3.6+-white.svg?logo=python)](https://www.python.org/downloads)
[![Code Size](https://img.shields.io/github/languages/code-size/Tes3awy/HEX-to-IP-Conversion?color=green)](https://github.com/Tes3awy/HEX-to-IP-Conversion)
[![License](https://img.shields.io/github/license/Tes3awy/HEX-to-IP-Conversion)](https://github.com/Tes3awy/HEX-to-IP-Conversion)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Convert IPv4 Address to HEX IP and vice versa

This program is designed to convert an IPv4 Address to a HEX IP and vice versa.

> This program is useful for **Wireless** and **Collaboration** teams where they use the HEX IPs in DHCP pools.

**DHCP Pools Example**

```cisco
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
```

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Usage](#usage)
   - [IP to HEX](#ip-to-hex)
   - [HEX to IP](#hex-to-ip)

### Getting Started

```bash
│   main.py
│   ip_to_hex.py
│   hex_to_ip.py
│   requirements.txt
│   .pre-commit-config.yaml
│   README.md
│   .gitignore
│   LICENSE
│
└───assets
      1.png
      2.png
      3.png
      4.png
```

### Installation

```bash
$ git clone https://github.com/Tes3awy/HEX-to-IP-Conversion.git
$ cd HEX-to-IP-Conversion
$ pip install -r requirements.txt --user
```

### Usage

**Windows**

```powershell
python main.py
```

**macOS and \*nix**

```bash
python3 main.py
```

You will be prompted to enter one of two values: `[1/2]`

> 1 is to convert from IPv4 to HEX.

> 2 is to convert from HEX to IPv4.

#### IP to HEX

![1](assets/1.png)
![2](assets/2.png)

#### HEX to IP

![3](assets/3.png)
![4](assets/4.png)
