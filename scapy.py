#!/usr/bin/python

import scapy


ls()
ls(IP)
IP().show()
lsc()
conf

#Sniffing packets

pkts=sniff(iface="eth1",count=3)

hexdump()

# simulation snifffering with a offfline pacp capture

pkts=sniff(offline="offline.pcap")


# Addning Filters

pkts=sniff(iface="eth1",filter="arp", count=3)

# Print packets live

pkts=sniff(iface="eth1",filter="icmp",count=20,prn=lambda x: x.summary())

# Write packes to a pcap file


wrpcap("demo.cap",pkts)

# read from pcap

rdpcap("demo.cap")

# export packet as Base64 encoded

export_object(str(pkts[0]))


icmp_string=str(pkts[7])

icmp_string

recon=Ether(icmp_string)




>>> newPkt=import_object()
eNprYApN2qH+WsJFjSEhJbTMhoPBlYEhhAEIzBj/vFpzU1LvwApGfgaG+fwsyQwsm36xRO8wYGLg
4OTi5uHl4xcQFBIWERUTl5CUkpaRlZNXUFRSVlFVU9fQ1NLW0dXTNzA0MjYxNTMvZNQDADt9Fek=
>>> newPkt
'\xb8\'\xeb\x18D&\x00`dUv<\x08\x00E\x00\x00T\x00\x00\x00\x006\x01\xfc\xea\xac\xd9\x19.\xc0\xa8\x01\x0f\x00\x00\x9f\x0f\x04c\x00\x04\xb2\xfa\x04[\xb80\x02\x00\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'
>>> 




