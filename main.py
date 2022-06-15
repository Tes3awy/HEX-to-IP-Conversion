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
# Version: Python 3.10.5
# Author: Osama Abbas (oabbas2512@gmail.com)
# Description:   This program is designed to convert from IPv4 Address to
#                HEX IP and vice versa.
#
# ------------------------------------------------------------------------

from rich import print

from conversion import Convert


def main():
    print(
        "[magenta][1] IPv4 to Hex[/magenta]\n[blue][2] HEX to IPv4[/blue]", end="\n\n"
    )
    try:
        CHOICE = int(input("Enter 1 or 2 [Default 1]: ").strip() or "1")

        # Convert from IPv4 to HEX
        if CHOICE == 1:
            ip_addr = input("IPv4 Address: ").strip() or "192.168.1.1"
            hex_addr = Convert.to_hex(ip_addr)
            print(
                f"HEX Address of [green]{ip_addr}[/green] is [magenta]{'.'.join(hex_addr[i : i + 2] for i in range(0, len(hex_addr), 2))}[/magenta]"
            )
        # Convert from HEX to IPv4
        elif CHOICE == 2:
            hex_addr = input("HEX Address: ").strip().lower() or "c0.a8.01.01"
            ipaddr = Convert.to_ip(hex_addr)
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
