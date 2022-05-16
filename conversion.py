# -*- coding: utf-8 -*-
import socket
import struct

from netaddr import *


class Convert:
    def __init__(self, value: str) -> None:
        self.value = value

    def to_ip(self) -> str:
        hex_val = self.value.replace(".", "")
        ip_val = int(hex_val.lower(), 16)
        return socket.inet_ntoa(struct.pack(">L", ip_val))

    def to_hex(self) -> str:
        return socket.inet_aton(self.value).hex().lower()
