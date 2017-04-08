import sys, socket, getopt, threading, subprocess

#define some global variables
listen             = False
command            = False
upload             = False
execute            = ""
target             = ""
upload_destination = ""
port               = 0

def usage():
    print 'Welcome to the wonderous Netcat replacement that is Pycat'
    print
    print 'Usage: 
