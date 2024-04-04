import struct
from constants import TINY, ISP



def receive_packet(sock):
    buffer = b''

    while True:
        data = sock.recv(1024)

        if data:
            buffer += data 
            while len(buffer) > 0 and len(buffer) > buffer[0]:
                packet = buffer[:buffer[0]]
        
                buffer = buffer[buffer[0]:]

                process_packet(packet, sock)
        else: 
            break
    # sock.close()

def process_packet(packet, sock):
    if len(packet) <= 1:
        print('Invalid packet: ', packet)
        return
    
    if packet[1] == ISP.ISP_VER.value:
        size, type, reqi, zero, version, product, insimver = struct.unpack('BBBB8s6sH', packet)
        print(size, type, reqi, zero, version.decode("utf-8"), product.decode("utf-8"), insimver)
        print('Initialized insim.')
    elif packet[1] == ISP.ISP_TINY.value:
        # Unpack the packet data.
        tiny = struct.unpack('BBBB', packet)
        # Check the SubT.
        if tiny[3] == TINY.TINY_NONE.value:
            # Send the keep alive packet back to LFS.
            sock.send(packet)
            print('Sent keep alive packet.')
    elif packet[1] == ISP.ISP_MSO.value:
        size, type, reqI, zero, UCID, PLID, userType, textStart = struct.unpack('8B', packet[:8])
        message = struct.unpack('%dsx' % int(size - 9), packet[8:])[0]
        print(message.rstrip(b'\x00').decode('utf-8'))
    else:
        print('Received unknown packet type: ', packet[1])

def send_packet(socket, packet):
    socket.send(packet)


def send_message(socket, message):
    packet = struct.pack('4B63sx', 
                68,           # Size
                ISP.ISP_MST.value,            # Type
                0,            # ReqI  
                0,            # Zero                
                message) # IName
    
    send_packet(socket, packet)


def send_init_packet(socket):
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
                b'unga bunga',   # Admin
                b'PysimTesting',) # IName
    socket.send(isi)

