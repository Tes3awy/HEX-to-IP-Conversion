#!/usr/bin/env python3

# -------------------------------------------------------------------------------
#
# Demonstrates how to convert from IPv4 Address to HEX IP and vice versa
#
# (C) 2021 Osama Abbas, Cairo, Egypt
# Released under MIT License
#
# Filename: main.py
# Version: Python 3.9.5
# Authors: Osama Abbas (oabbas2512@gmail.com)
# Description:   This program is designed to convert from IPv4 Address to HEX IP
#                and vice versa.
#
# -------------------------------------------------------------------------------

from hex_to_ip import hex_to_ip
from ip_to_hex import ip_to_hex

print("\nConvert from IPv4 to Hex [1]")
print("Convert from HEX to IPv4 [2]")
CHOICE = input("[1/2]: ")

# Convert from IPv4 to HEX
if CHOICE == "1":
    IP_ADDR = input("Please enter one IPv4 Address: ")
    ip_to_hex(IP_ADDR)

# Convert from HEX to IPv4
elif CHOICE == "2":
    HEX_IP = input("Please enter one HEX Address: ")
    hex_to_ip(HEX_IP)

else:
    print("✖ Unknown input value! (Only values 1 or 2 are allowed).")
