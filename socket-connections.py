import os
import socket
# AI generated functions, for the most part they seemed to work but be sure to doubletest and review if errors occur

def sendData(host, port, line_to_send):
    try:
        # Create a TCP socket
        with socket.create_connection((host, port), timeout=5) as sock:
            print(f"Connected to {host}:{port}")

            # Send the line (make sure to end with newline if needed by the protocol)
            sock.sendall(line_to_send.encode() + b"\n")

            # Receive all available data
            sock.settimeout(2)  # Timeout after 2 seconds of no data
            response = b""

            while True:
                try:
                    chunk = sock.recv(4096)
                    if not chunk:
                        break
                    response += chunk
                except socket.timeout:
                    break  # No more data incoming, end reading

            return response.decode(errors='ignore')

    except Exception as e:
        print(f"Error: {e}")
        return None

def getLine(host, port):
    try:
        # Create a TCP socket
        with socket.create_connection((host, port), timeout=5) as sock:
            print(f"Connected to {host}:{port}")

            # Receive some data
            data = sock.recv(4096).decode(errors='ignore')

            # Split into lines
            lines = data.splitlines()

            if lines:
#                first_line = lines[0]
                return lines
            else:
                print("No data received.")
                return None

    except Exception as e:
        print(f"Connection error: {e}")
        return None

