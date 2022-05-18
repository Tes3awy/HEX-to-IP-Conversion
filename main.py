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

from conversion import Convert


def main():
    print("[magenta][1] Convert from IPv4 to Hex")
    print("[blue][2] Convert from HEX to IPv4")
    try:
        CHOICE = int(input("Please enter 1 or 2 [1]: ").strip() or "1")

        # Convert from IPv4 to HEX
        if CHOICE == 1:
            ip_addr = input("IPv4 Address: ").strip()
            hex_addr = Convert(value=ip_addr).to_hex()
            print(
                f"HEX value of [green]{ip_addr}[/green] is [magenta]{hex_addr}[/magenta]"
            )
        # Convert from HEX to IPv4
        elif CHOICE == 2:
            hex_addr = input("HEX Address: ").strip().lower()
            ipaddr = Convert(value=hex_addr).to_ip()
            print(f"IPv4 of [magenta]{hex_addr}[/magenta] is [green]{ipaddr}[/green]")
        else:
            print(
                "[red]:x: Invalid input value! (1 and 2 are the only allowed values)."
            )
    except KeyboardInterrupt:
        raise SystemExit(print("[yellow]\nAborted by the user! (Ctrl+C)")) from None
    except ValueError:
        raise SystemExit(
            print("[red]:x: Invalid value! Only Integer values (1 and 2) are allowed.")
        ) from None


if __name__ == "__main__":
    main()
