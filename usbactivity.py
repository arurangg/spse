#!/usr/bin/python

f = open("/var/log/syslog","r")
for line in f.readlines():
    if line.find("kernel") <> -1:
        print line
       


