# -*- coding: utf-8 -*-
import socket
import struct
import subprocess
import sys

from rich import print


def hex_to_ip(hex: str) -> None:
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
        hex = hex.replace(".", "")
        len(hex) <= 8
        HEX = int(hex.lower(), 16)
        IP_ADDR = socket.inet_ntoa(struct.pack(">L", HEX))
    except struct.error:
        raise SystemExit(
            print(
                f"[red]{hex} does not appear to be a HEX Address! (HEX is 8 bits only. Current length: {len(hex)})."
            )
        )
    else:
        subprocess.run(
            "clip", universal_newlines=True, input=IP_ADDR
        ) if sys.platform == "win32" else subprocess.run(
            "pbcopy", universal_newlines=True, input=IP_ADDR
        )

        print(f"[green]IPv4: {IP_ADDR} is copied to your clipboard.")
