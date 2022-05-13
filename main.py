#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------
#
# Demonstrates how to convert from IPv4 Address to HEX IP and vice versa
#
# (C) 2021-2022 Osama Abbas, Cairo, Egypt
# Released under MIT License
#
# Filename: main.py
# Version: Python 3.10.4
# Author: Osama Abbas (oabbas2512@gmail.com)
# Description:   This program is designed to convert from IPv4 Address to
#                HEX IP and vice versa.
#
# ------------------------------------------------------------------------

import subprocess
import sys

from rich import print

from hex_to_ip import hex_to_ip
from ip_to_hex import ip_to_hex


def main():
    print("[magenta][1] Convert from IPv4 to Hex")
    print("[blue][2] Convert from HEX to IPv4")
    try:
        CHOICE = int(input("Enter 1 or 2: ").strip() or "1")

        # Convert from IPv4 to HEX
        if CHOICE == 1:
            IP_ADDR = input("Please enter one IPv4 Address: ").strip()
            hex_val = ip_to_hex(ip=IP_ADDR)
            subprocess.run(
                "clip", universal_newlines=True, input=hex_val
            ) if sys.platform == "win32" else subprocess.run(
                "pbcopy", universal_newlines=True, input=hex_val
            )
            print(f"HEX value of {IP_ADDR} is [magenta]{hex_val}[/magenta]")
        # Convert from HEX to IPv4
        elif CHOICE == 2:
            HEX_IP = input("Please enter one HEX Address: ").strip()
            ipaddr = hex_to_ip(hex=HEX_IP)
            subprocess.run(
                "clip", universal_newlines=True, input=ipaddr
            ) if sys.platform == "win32" else subprocess.run(
                "pbcopy", universal_newlines=True, input=ipaddr
            )
            print(f"IPv4 address of {HEX_IP} is [magenta]{ipaddr}[/magenta]")
        else:
            print(
                "[red]:x: Invalid input value! (1 and 2 are the only allowed values)."
            )
    except KeyboardInterrupt:
        raise SystemExit(print("[yellow]\nAborted by the user! (Ctrl+C)")) from None
    except ValueError:
        raise SystemExit(
            print("[red]Invalid value! Only Integer values are supported.")
        ) from None


if __name__ == "__main__":
    main()
