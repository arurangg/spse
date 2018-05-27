#!/usr/bin/python

myBio={'name':'vivek','age':31,'hobby':'hacking'}

print myBio

print myBio.has_key('hobby')

print myBio.has_key('hobbies')

print myBio.keys()

print myBio.values()

print myBio.items()


print myBio.get('age')

myBio['location']='India'

print myBio



# del myBio['location']
# myBio.clear()

print dir(myBio)

print help(myBio.has_key)
