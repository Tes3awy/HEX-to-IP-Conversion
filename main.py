#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------
#
# Demonstrates how to convert from IPv4 Address to HEX IP and vice versa
#
# (C) 2021 Osama Abbas, Cairo, Egypt
# Released under MIT License
#
# Filename: main.py
# Version: Python 3.9.10
# Author: Osama Abbas (oabbas2512@gmail.com)
# Description:   This program is designed to convert from IPv4 Address to
#                HEX IP and vice versa.
#
# ------------------------------------------------------------------------

from rich import print

from hex_to_ip import hex_to_ip
from ip_to_hex import ip_to_hex


def main():
    print("Convert from IPv4 to Hex [1]")
    print("Convert from HEX to IPv4 [2]")
    try:
        CHOICE = int(input("Enter 1 or 2 [1/2]: ").strip()) or 1

        # Convert from IPv4 to HEX
        if CHOICE == 1:
            IP_ADDR = input("Please enter one IPv4 Address: ").strip()
            ip_to_hex(ip=IP_ADDR)

        # Convert from HEX to IPv4
        elif CHOICE == 2:
            HEX_IP = input("Please enter one HEX Address: ").strip()
            hex_to_ip(hex=HEX_IP)

        else:
            print("[red]✖ Invalid input value!")
    except KeyboardInterrupt:
        raise SystemExit(print("[yellow]Process interrupted by the user"))


if __name__ == "__main__":
    main()
