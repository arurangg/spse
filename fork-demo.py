#!/usr/bin/python


import os



def child_process():
    
    print "I am the child process and my PID is: %d"%os.getpid()

    print "The child is exiting"

def parent_process():
    
    print "I am a the parent proecess with PID :%d"%os.getpid()
    
    childpid=os.fork()

    if  childpid==0:
        # We are inside the child
        child_process()
    else:
        # we are inside the parent process
        print "We are inside the parent process"
        print "Out child has the PID: %d" %childpid

    while True:
        pass


parent_process()




