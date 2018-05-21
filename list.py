#!/usr/bin/python

mylist=[1,2,3]

len1=len(mylist)

print len1

print mylist[0]
print mylist[1]
print mylist[2]


mynestedlist=[1,2,[3,4]]

print len(mynestedlist)


print len(mynestedlist[2])

heterogeneousList=[1,"vivek",3,"hello"]

print '========\n'
print len(heterogeneousList[3])

heterogeneousList.append("Python Master")

print heterogeneousList
heterogeneousList.reverse()
print heterogeneousList
print heterogeneousList.pop()

heterogeneousList.insert(2,"there")
print heterogeneousList

del heterogeneousList[2]

print heterogeneousList


