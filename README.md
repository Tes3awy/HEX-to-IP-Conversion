[![Visual Studio Code](https://img.shields.io/badge/VSCode-1.57.0-blue.svg?logo=visual-studio-code)](https://code.visualstudio.com/)
[![Tested on Python 3.6+](https://img.shields.io/badge/Tested%20-Python%203.6-blue.svg?logo=python)](https://www.python.org/downloads)
[![Code Size](https://img.shields.io/github/languages/code-size/Tes3awy/HEX-to-IP-Conversion?color=green)](https://github.com/Tes3awy/HEX-to-IP-Conversion)
[![License](https://img.shields.io/github/license/Tes3awy/HEX-to-IP-Conversion)](https://github.com/Tes3awy/HEX-to-IP-Conversion)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# Convert IPv4 Address to HEX IP and vice versa

This program is designed to convert an IPv4 Address to a HEX IP and vice versa.

> This program is useful for **Wireless** and **Collaboration** teams where they use the HEX IPs in DHCP pools;

**Example:**

```cisco
ip dhcp pool APs
   network 172.16.1.0 255.255.0.0
   default-router 172.16.1.1
   option 43 hex f104.c0a8.0a05
exit
```

## Table of Contents

1. [Installation](#installation)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
   1. [IP to HEX](#ip-to-hex)
   2. [HEX to IP](#hex-to-ip)

### Installation

```bash
$ git clone https://github.com/Tes3awy/HEX-to-IP-Conversion.git
$ cd HEX-to-IP-Conversion
$ pip install -r requirements.txt --user
```

### Getting Started

```bash
│   main.py
│   ip_to_hex.py
│   hex_to_ip.py
│   requirements.txt
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

### Usage

**Windows**

```powershell
python main.py
```

**macOS and Linux**

```bash
python3 main.py
```

You will be prompted to enter one of two values: `[1/2]`.

> 1 is to convert from IPv4 to HEX

> 2 is to convert from HEX to IPv4

#### IP to HEX

![1](assets/1.png)
![2](assets/2.png)

#### HEX to IP

![3](assets/3.png)
![4](assets/4.png)
