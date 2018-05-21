#!/usr/bin/python


import subprocess

#subprocess.call(['ps','aux'])

#subprocess.call(['ls','-al'])



#lis=subprocess.check_output(['ls','-al'])

#print lis




handle=subprocess.Popen("ls",stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)






