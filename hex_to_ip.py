import socket
import struct
import subprocess
import sys

from termcolor import colored, cprint


def hex_to_ip(hex: str) -> None:
    """Converts HEX to IPv4

    Args:
        hex (str): HEX IP Address
    """
    try:
        hex = hex.replace(".", "")
        len(hex) <= 8
        HEX = int(hex.lower(), 16)
        IP_ADDR = socket.inet_ntoa(struct.pack(">L", HEX))
    except struct.error:
        raise SystemExit(
            colored(
                f"'{hex}' is an invalid HEX Address! (HEX is 8 bits only. Current length: {len(hex)}).",
                "red",
            )
        )
    else:
        subprocess.run(
            "clip", universal_newlines=True, input=IP_ADDR
        ) if sys.platform == "win32" else subprocess.run(
            "pbcopy", universal_newlines=True, input=IP_ADDR
        )

        cprint(text=f"IPv4: '{IP_ADDR}' is copied to your clipboard.", color="green")
