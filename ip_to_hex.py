# -*- coding: utf-8 -*-
import socket
import subprocess
import sys

from netaddr import *
from netaddr import AddrFormatError
from rich import print


def ip_to_hex(ip: str) -> None:
    """Convert IPv4 to HEX

    Parameters
    ----------
    ip : str
        IPv4 Address

    Raises
    ------
    SystemExit
        AddrFormatError
    """
    try:
        IPAddress(ip).version == 4
    except AddrFormatError as e:
        raise SystemExit(
            print(f"[red]{ip} does not appear to be an IPv4 address!")
        ) from e

    else:
        HEX = socket.inet_aton(ip).hex().lower()
        subprocess.run(
            "clip", universal_newlines=True, input=HEX
        ) if sys.platform == "win32" else subprocess.run(
            "pbcopy", universal_newlines=True, input=HEX
        )

        print(f"[green]Hex: {HEX} is copied to your clipboard.")
