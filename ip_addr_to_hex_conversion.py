import socket
import struct
from netaddr import *

print("To convert from IP Address to Hex enter 1")
print("To convert from HEX to IP Address enter 2")
CHOICE = input("[1/2]: ")

if CHOICE == "1":
    try:
        IP_ADDR = input("Please enter one v4 IP Address: ")
        IPAddress(IP_ADDR).version == 4
        try:
            HEX = socket.inet_aton(IP_ADDR).hex().lower()
            print(f"✔ Hex IP: {HEX}")
        except:
            print(f"'❌ {IP_ADDR}' is an invalid v4 IP address!")
    except core.AddrFormatError as e:
        print(f"'{IP_ADDR}' is an invalid v4 IP address!")
elif CHOICE == "2":
    try:
        HEX = input("Please enter one HEX IP Address: ")
        HEX = HEX.replace(".", "")
        len(HEX) <= 8
        try:
            HEX = int(HEX.lower(), 16)
            IP_ADDR = socket.inet_ntoa(struct.pack(">L", HEX))
            print(f"✔ v4 IP Address: {IP_ADDR}")
        except:
            print(f"'{HEX}' is an invalid HEX Address!")
    except:
        print(f"'{HEX}' is an invalid HEX Address!")
else:
    print("❌ Unknown input value!")
