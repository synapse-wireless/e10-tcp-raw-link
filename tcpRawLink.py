'''tcpRawLink -- Transparent serial gateway for SNAP Link applications'''

# Port number for "raw serial" connection over TCP
TCP_PORT = 3000
MCAST_TTL = 3

import sys
import binascii
import asyncore
import socket
from snapconnect import snap

import logging
log = logging.getLogger()

# Note the hardcoded COM1 usage.
# You should set these to match YOUR available hardware
SERIAL_TYPE = snap.SERIAL_TYPE_RS232
#SERIAL_TYPE = snap.SERIAL_TYPE_SNAPSTICK100
#SERIAL_TYPE = snap.SERIAL_TYPE_SNAPSTICK200

# If you're on a unix platform, you'll need to specify the interface type differently than windows
# An example for a typical interface device is shown below
#SERIAL_PORT = 0 # COM1
SERIAL_PORT = '/dev/ttyS1'

class TcpHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(96)
        if data:
            snapCom.mcast_data_mode(1, MCAST_TTL, data)


class TcpServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.handler = None

    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            pass
        else:
            sock, addr = pair
            log.info('Incoming connection from %s' % repr(addr))
            if self.handler != None:
                try:
                    # New connections "bump" old ones
                    self.handler.close()
                except:
                    pass

            self.handler = TcpHandler(sock)


def rxDataMode(data):
    #log.debug("rxDataMode")

    if server.handler != None:
        try:
            server.handler.send(data)
        except:
            pass

def main():
    global server, snapCom

    # Listen for raw-TCP connections
    server = TcpServer('', TCP_PORT)

    # Create SNAP instance and establish serial (bridge) link
    snapCom = snap.Snap(funcs={})
    snapCom.open_serial(SERIAL_TYPE, SERIAL_PORT)

    # Setup to receive data-mode packets
    snapCom.set_hook(snap.hooks.HOOK_STDIN, rxDataMode)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(msecs)03d %(levelname)-8s %(name)-8s %(message)s', datefmt='%H:%M:%S')

    main()
    snapCom.loop()
