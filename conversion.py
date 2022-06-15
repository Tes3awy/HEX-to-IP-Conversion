# -*- coding: utf-8 -*-
from socket import inet_aton, inet_ntoa
from struct import pack


class Convert:
    @staticmethod
    def to_ip(__hexaddr: str, /) -> str:
        """
        Convert from HEX Address to IPv4

        Parameters
        ----------
        __hexaddr : str
            HEX Address. Example: c0a80101

        Returns
        -------
        str
            IPv4 Address
        """
        hex_val = __hexaddr.replace(".", "")
        return inet_ntoa(pack(">L", int(hex_val.lower(), 16)))

    @staticmethod
    def to_hex(__ipaddr: str, /) -> str:
        """
        Convert from IPv4 to HEX Address

        Parameters
        ----------
        __ipaddr : str
            IPv4 Address. Example: 192.168.1.1

        Returns
        -------
        str
            HEX Address
        """
        return inet_aton(__ipaddr).hex().lower()
