#!/usr/bin/python



pkt=IP(dst="google.com")


pkt=IP(dst="google.com")/ICMP()/"Vivek was here"

pkt.show()



# Scapy Injection and Forging

sendp(Ether()/IP(dst="google.com")/ICMP()/"XXXX",iface="eth1",loop=1,inter=1)

# Send and Receive

srp1(Ether()/IP(dst="google.com",ttl=22)/ICMP()/"XXX")
sr(IP(dst="google.com",ttl=22)/ICMP()/"XXX")
sr1(IP(dst="google.com"), timeout=3)


# routing 

conf.route.add(host="192.168.1.10",gw="192.168.1.22")
conf.route.resync()




