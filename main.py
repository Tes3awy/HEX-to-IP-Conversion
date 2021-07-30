#!/usr/bin/python3

# ------------------------------------------------------------------------
#
# Demonstrates how to convert from IPv4 Address to HEX IP and vice versa
#
# (C) 2021 Osama Abbas, Cairo, Egypt
# Released under MIT License
#
# Filename: main.py
# Version: Python 3.9.6
# Author: Osama Abbas (oabbas2512@gmail.com)
# Description:   This program is designed to convert from IPv4 Address to
#                HEX IP and vice versa.
#
# ------------------------------------------------------------------------

from colorama import init
from termcolor import colored, cprint

from hex_to_ip import hex_to_ip
from ip_to_hex import ip_to_hex

init(autoreset=True)


def main():
    print("Convert from IPv4 to Hex [1]")
    print("Convert from HEX to IPv4 [2]")
    try:
        CHOICE = input("[1/2]: ").strip()

        # Convert from IPv4 to HEX
        if CHOICE == "1":
            IP_ADDR = input("Please enter one IPv4 Address: ").strip()
            ip_to_hex(ip=IP_ADDR)

        # Convert from HEX to IPv4
        elif CHOICE == "2":
            HEX_IP = input("Please enter one HEX Address: ").strip()
            hex_to_ip(hex=HEX_IP)

        else:
            cprint(
                text="✖ Unknown input value! (1 or 2 are the only allowed values).",
                color="red",
            )
    except KeyboardInterrupt:
        raise SystemExit(
            colored(text="Process interrupted by the user", color="yellow")
        )


if __name__ == "__main__":
    main()
