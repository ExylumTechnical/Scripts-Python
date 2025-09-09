import socket

def udp_send(addr,port,message):
    print("UDP target IP: %s" % addr)
    print("UDP target port: %s" % port)
    print("message: %s" % message)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(message.encode(), (addr, port))
message=input("Reason for access:")
udp_send("YOURGLORIOUSIP",514,message
