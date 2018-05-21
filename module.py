#!/usr/bin/python


import classformodule

print 'quick Add a+b: %d' %classformodule.quickAdd(10,20)

res=classformodule.Scientific(7,6)

print "a+b: %d"%res.add()

print "aXb: %d"%res.mul()

ad=str(res.power())

list1=list(ad)
total=0

for item in list1:

    total=total+int(item)


print total

print list1

print ad

print "a POW b: %d"%res.power()

