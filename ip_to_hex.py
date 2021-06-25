#!/usr/bin/env python3

import socket
import subprocess
import sys

from netaddr import *
from netaddr import core


def ip_to_hex(IP_ADDR: str):
    """Converts IPv4 to HEX

    Args:
        IP_ADDR (str): IPv4 Address
    """
    try:
        IPAddress(IP_ADDR).version == 4
        HEX = socket.inet_aton(IP_ADDR).hex().lower()
    except core.AddrFormatError:
        print(f"✖ '{IP_ADDR}' is an invalid IPv4 address!", file=sys.stderr)
    else:
        if sys.platform == "win32":
            subprocess.run("clip", universal_newlines=True, input=HEX)
        else:
            subprocess.run("pbcopy", universal_newlines=True, input=HEX)
        print(f"✔ Hex IP: {HEX}. '{HEX}' is copied to your clipboard.")
