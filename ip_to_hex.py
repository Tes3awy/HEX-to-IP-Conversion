import socket
import subprocess
import sys

from netaddr import *
from netaddr import AddrFormatError
from termcolor import colored, cprint


def ip_to_hex(ip: str) -> None:
    """Converts IPv4 to HEX

    Args:
        ip (str): IPv4 Address
    """
    try:
        IPAddress(ip).version == 4
        HEX = socket.inet_aton(ip).hex().lower()
    except AddrFormatError:
        raise SystemExit(colored(f"'{ip}' is an invalid IPv4 address!", "red"))
    else:
        subprocess.run(
            "clip", universal_newlines=True, input=HEX
        ) if sys.platform == "win32" else subprocess.run(
            "pbcopy", universal_newlines=True, input=HEX
        )

        cprint(text=f"Hex: '{HEX}' is copied to your clipboard.", color="green")
