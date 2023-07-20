# -*- coding: utf-8 -*-
from socket import inet_aton, inet_ntoa
from struct import pack


class Convert:
    def __init__(self, value: str) -> None:
        self.value = value

    def to_ip(self) -> str:
        hex_val = self.value.replace(".", "")
        ip_val = int(hex_val, 16)
        return inet_ntoa(pack(">L", ip_val))

    def to_hex(self) -> str:
        return inet_aton(self.value).hex()
