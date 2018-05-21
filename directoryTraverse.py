#!/usr/bin/python


import os

import glob

for it in glob.glob(os.path.join(".","*.py")):
    print it

print os.getcwd()

#os.mkdir("NewDir")

print os.listdir(".")


print os.listdir("/")

for item in os.listdir("."):
    if os.path.isfile(item):
        print item +" is a file"
    elif os.path.isdir(item):
        print item+" is a Directory"

    else:
        print "Unknown!"




