#!/usr/bin/python

import socket
import struct
import binascii


rawSocket=socket.socket(socket.PF_PACKET,socket.SOCK_RAW, socket.htons(0X0800))

pkt=rawSocket.recvfrom(2048)

ethernetHeader=pkt[0][0:14]

eth_hdr=struct.unpack("!6s6s2s",ethernetHeader)

binascii.hexlify(eth_hdr[0])
binascii.hexlify(eth_hdr[1])
binascii.hexlify(eth_hdr[2])

ipHeader=pkt[0][14:34]

ip_hdr=struct.unpack("!12s4s4s",ipHeader)

print "Source IP address: "+ socket.inet_ntoa(ip_hdr[1])

print "Destination IP address: "+ socket.inet_ntoa(ip_hdr[2])

#Initial part of the tcp header

tcpHeader=pkt[0][34:54]

tcp_hdr=struct.unpack("!HH16s",tcpHeader)




one=struct.pack("B",1)
unsignshort=struct.pack("H",1)
ideam=struct.pack(">H",1)
ide=struct.pack("!H",1)

unsignlonginteger=struct.pack("!L",1)


reverse=struct.unpack("!L",1)




