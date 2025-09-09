import os
import socket
hostname=socket.gethostname()
ip_address=socket.gethostbyname_ex(hostname)
ifname=socket.if_nameindex()
print(ip_address)
print(ifname)
network=""
