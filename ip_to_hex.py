#!/usr/bin/env python
import sys
import subprocess
import socket
import struct
from netaddr import *


# Convert from IPv4 to Hex
def ip_to_hex(IP_ADDR):
    try:
        IPAddress(IP_ADDR).version == 4
        HEX = socket.inet_aton(IP_ADDR).hex().lower()
        if sys.platform == "win32":
            subprocess.run("clip", universal_newlines=True, input=HEX)
        else:
            subprocess.run("pbcopy", universal_newlines=True, input=HEX)
        print(f"✔ Hex IP: {HEX}. '{HEX}' is copied to your clipboard.")
        return True
    except core.AddrFormatError:
        print(f"✖ '{IP_ADDR}' is an invalid IPv4 address!")