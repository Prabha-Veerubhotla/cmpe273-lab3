from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class HelloerServer(DatagramProtocol):

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))
        if (data == b"Client: hello"):
            self.transport.write(b"Server: Hello", addr)
        

reactor.listenUDP(9991, HelloerServer())
reactor.run()