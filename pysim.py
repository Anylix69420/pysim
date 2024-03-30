import socket
import struct
from util import send_packet, receive_packet

class LFSInSim:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.connect((self.host, self.port))

    def close(self):
        self.socket.close()

if __name__ == "__main__":
    insim = LFSInSim("127.0.0.1", 29999)
    try:
        send_packet(insim.socket)
        receive_packet(insim.socket)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        insim.close()
