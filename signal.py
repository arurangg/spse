#!/usr/bin/python


import signal

def ctrl_handler(signum,frm):
    print "\n Haha! You cannot kill me!"


print "Installing signal handler...."


signal.signal(signal.SIGINT, ctrl_handler)

print "Done!"

while True:
    pass




