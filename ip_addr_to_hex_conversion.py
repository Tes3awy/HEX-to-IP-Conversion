#!/usr/bin/env python

# -------------------------------------------------------------------------------
#
# Demonstrates how to convert from IPv4 Address to HEX IP and vice versa
#
# (C) 2021 Osama Abbas, Cairo, Egypt
# Released under MIT License
#
# Filename: ip_addr_to_hex_conversion.py
# Version: Python 3.9.4
# Authors: Osama Abbas (oabbas2512@gmail.com)
# Description:   This program is designed to convert from IPv4 Address to HEX IP
#                and vice versa.
#
# -------------------------------------------------------------------------------

import socket
import struct
from netaddr import *

print("To convert from IP Address to Hex enter 1")
print("To convert from HEX to IP Address enter 2")
CHOICE = input("[1/2]: ")

# Convert from IPv4 Address to HEX IP
if CHOICE == "1":
    IP_ADDR = input("Please enter one IPv4 Address: ")
    try:
        IPAddress(IP_ADDR).version == 4
        HEX = socket.inet_aton(IP_ADDR).hex().lower()
        print(f"✔ Hex IP: {HEX}")
    except core.AddrFormatError:
        print(f"✖ '{IP_ADDR}' is an invalid IPv4 address!")

# Convert from HEX IP to IPv4 Address
elif CHOICE == "2":
    HEX_IP = input("Please enter one HEX IP Address: ")
    HEX_IP = HEX_IP.replace(".", "")
    try:
        len(HEX_IP) <= 8
        HEX = int(HEX_IP.lower(), 16)
        IP_ADDR = socket.inet_ntoa(struct.pack(">L", HEX))
        print(f"✔ IPv4 Address: {IP_ADDR}")
    except:
        print(f"✖ '{HEX_IP}' is an invalid HEX Address! (HEX IP is 8 bits only)")
else:
    print("✖ Unknown input value! (Only values 1 or 2 are allowed)")
