import struct
import constants
def receive_packet(sock):
    buffer = b''

    while True:
        data = sock.recv(1024)

        if data:
            buffer += data 
            while len(buffer) > 0 and len(buffer) > buffer[0]:
                packet = buffer[:buffer[0]]
        
                buffer = buffer[buffer[0]:]

                process_packet(packet)
        else: 
            break
    sock.close()

def process_packet(packet):
    size, type, reqi, zero, version, product, insimver = struct.unpack('BBBB8s6sH', packet)
    print(size, type, reqi, zero, version.decode("utf-8"), product.decode("utf-8"), insimver)
    print('Received')

def send_packet(socket):
    isi = struct.pack('BBBBHHBcH16s16s', 
                44,           # Size
                1,            # Type
                1,            # ReqI  
                0,            # Zero
                0,            # UDPPort
                0,            # Flags
                0,            # Sp0
                b' ',          # Prefix
                0,            # Interval
                b'password',   # Admin
                b'MyProgram',) # IName
    socket.send(isi)
    print('Sent')

