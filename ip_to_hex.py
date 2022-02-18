import socket
import subprocess
import sys

from netaddr import *
from rich import print


def ip_to_hex(ip: str) -> None:
    """Converts IPv4 to HEX

    Args:
        ip (str): IPv4 Address
    """
    try:
        IPAddress(ip).version == 4
        HEX = socket.inet_aton(ip).hex().lower()
    except AddrFormatError as e:
        raise SystemExit(print(f"[red]'{ip}' is an invalid IPv4 address!")) from e
    else:
        subprocess.run(
            "clip", universal_newlines=True, input=HEX
        ) if sys.platform == "win32" else subprocess.run(
            "pbcopy", universal_newlines=True, input=HEX
        )

        print(f"[green]Hex: '{HEX}' is copied to your clipboard!", end="\n\n")
