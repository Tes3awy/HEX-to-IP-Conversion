# -*- coding: utf-8 -*-
import socket
import struct

from rich import print


def hex_to_ip(hex: str) -> str:
    """Convert Hex to IPv4 Address

    Parameters
    ----------
    hex : str
        Hex IP Address

    Raises
    ------
    SystemExit
        struct.error
    """
    try:
        hex_val = hex.replace(".", "")
        len(hex_val) <= 8
        HEX = int(hex_val.lower(), 16)
        IP_ADDR = socket.inet_ntoa(struct.pack(">L", HEX))
    except struct.error as e:
        raise SystemExit(
            print(
                f"[red]{hex_val} does not appear to be a valid HEX Address! (HEX is 8 bits only. Current length: {len(hex_val)})."
            )
        ) from e

    else:
        return IP_ADDR
