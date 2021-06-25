#!/usr/bin/env python3

import socket
import struct
import subprocess
import sys


def hex_to_ip(HEX_IP: str):
    """Converts HEX to IPv4

    Args:
        HEX_IP (str): HEX IP Address
    """
    try:
        HEX_IP = HEX_IP.replace(".", "")
        len(HEX_IP) <= 8
        HEX = int(HEX_IP.lower(), 16)
        IP_ADDR = socket.inet_ntoa(struct.pack(">L", HEX))
    except struct.error:
        print(
            f"✖ '{HEX_IP}' is an invalid HEX Address! (HEX is 8 bits only. Current length: {len(HEX_IP)}).",
            file=sys.stderr,
        )
    else:
        if sys.platform == "win32":
            subprocess.run("clip", universal_newlines=True, input=IP_ADDR)
        else:
            subprocess.run("pbcopy", universal_newlines=True, input=IP_ADDR)
        print(f"✔ IPv4 Address: {IP_ADDR}. '{IP_ADDR}' is copied to your clipboard.")
