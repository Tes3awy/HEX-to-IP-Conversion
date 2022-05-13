# -*- coding: utf-8 -*-
import socket

from netaddr import *
from netaddr import AddrFormatError
from rich import print


def ip2hex(ip: str) -> str:
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
        IPAddress(addr=ip).version == 4
    except AddrFormatError as e:
        raise SystemExit(
            print(f"[red]{ip} does not appear to be a valid IPv4 address!")
        ) from e

    else:
        return socket.inet_aton(ip).hex().lower()
