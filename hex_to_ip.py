#!/usr/bin/env python
import sys
import subprocess
import socket
import struct


# Convert from Hex to IPv4
def hex_to_ip(HEX_IP):
    HEX_IP = HEX_IP.replace(".", "")
    try:
        len(HEX_IP) <= 8
        HEX = int(HEX_IP.lower(), 16)
        IP_ADDR = socket.inet_ntoa(struct.pack(">L", HEX))
        if sys.platform == "win32":
            subprocess.run("clip", universal_newlines=True, input=IP_ADDR)
        else:
            subprocess.run("pbcopy", universal_newlines=True, input=IP_ADDR)
        print(f"✔ IPv4 Address: {IP_ADDR}. '{IP_ADDR}' is copied to your clipboard.")
    except:
        print(
            f"✖ '{HEX_IP}' is an invalid HEX Address! (HEX is 8 bits only. Current length: {len(HEX_IP)})."
        )