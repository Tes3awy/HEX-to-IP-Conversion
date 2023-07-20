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

from rich import print

from convert import Convert


def main():
    print("[magenta]1. Convert from IPv4 to Hex")
    print("[blue]2. Convert from HEX to IPv4", end="\n\n")
    try:
        CHOICE = int(input("Enter 1 or 2 [Default 1]: ").strip() or "1")
        match CHOICE:
            case 1:
                ip_addr = input("IPv4 Address: ").strip()
                hex_addr = Convert(value=ip_addr).to_hex()
                print(f"HEX value of is [magenta]{hex_addr}[/magenta]")
            case 2:
                hex_addr = input("HEX Address: ").strip().lower()
                ipaddr = Convert(value=hex_addr).to_ip()
                print(f"IPv4 of is [green]{ipaddr}[/green]")
            case _:
                print("[red]:x: Invalid value!")
    except KeyboardInterrupt as e:
        raise SystemExit(print("[yellow]\nAborted by the user! (Ctrl+C)")) from e
    except ValueError as e:
        raise SystemExit(
            print("[red]:x: Invalid value! Only Integers are allowed.")
        ) from e


if __name__ == "__main__":
    main()
