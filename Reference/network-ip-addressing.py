import os
import socket
hostname=socket.gethostname()
ip_address=socket.gethostbyname_ex(hostname)
ifname=socket.if_nameindex()
print(ip_address)
print(ifname)

# the above is usefull but will often only return the link local address

# the below will print the first available non link-local address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('google.com', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
print(get_ip())