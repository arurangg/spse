#!/usr/bin/python


import socket
import struct


rawSocket=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0X0800))

rawSocket.bind(("enp7s0",socket.htons(0X0800)))

packet=struct.pack("!6s6s2s",'\xaa\xaa\xaa\xaa\xaa\xaa','\xbb\xbb\xbb\xbb\xbb\xbb','\x08\x00')

#rawSocket.send(packet+"Hello there")




for i in range(99999):
      print "Hello there :"+str(i)
      rawSocket.send(packet+"Hello there :"+str(i))



