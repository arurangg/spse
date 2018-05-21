#!/usr/bin/python

s1="Aruran"
s2="Ganeshan"
buf="A"*20

print s1+' '+s2
print buf
s=s1+s2
print s[1:5]
print s.find('app')
print s.split('a')
print s.replace('Aru','anu')


ip="192.168.1.10"
line="Crack this IP: %s" %ip
line1="Crack this IP: %s and name %s" %(ip,"securitytube")

print line
print line1


