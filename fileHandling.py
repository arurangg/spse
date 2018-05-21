#!/usr/bin/python


fdesc=open("spse.txt","w")

for count in range(0,100):
    fdesc.write(str(count)+'\n')

fdesc.close()


fdesc=open("spse.txt","a")

for count in range(110,299):
        fdesc.write(str(count)+'\n')


fdesc.close()


fdesc=open("spse.txt","r")

for line in fdesc.readlines():
    print line.strip()

fdesc.close()
