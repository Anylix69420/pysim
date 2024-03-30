import struct
def receive_packet(sock):
    buffer = b''

    while True:
        # Receive up to 1024 bytes of data.
        data = sock.recv(1024)

        # If no data is received the connection has closed.
        if data:
            # Append received data onto the buffer.
            buffer += data
            # if len(buffer)>0:
            #     print(buffer[0])

            # Loop through each completed packet in the buffer. The first byte of
            # each packet is the packet size, so check that the length of the
            # buffer is at least the size of the first packet. 
            while len(buffer) > 0 and len(buffer) > buffer[0]:
                # Copy the packet from the buffer.
                packet = buffer[:buffer[0]]
        
                # Remove the packet from the buffer.
                buffer = buffer[buffer[0]:]

                # The packet is now complete! :)
                process_packet(packet)
        else: 
            break

    # Release the socket.
    sock.close()

def process_packet(packet):
    size, type, reqi, zero, version, product, insimver = struct.unpack('BBBB8s6sH', packet)
    print(size, type, reqi, zero, version.decode("utf-8"), product.decode("utf-8"), insimver)
    print('Received')

def send_packet(socket):
    #size = len(packet) + 1  # Add 1 for the size byte
    #self.socket.send(struct.pack("<B", size) + packet)
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

