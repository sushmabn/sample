import sys
from sys import argv

def console_logs(Finished):
    print "entry to code"
    if(string(Finished) == "SUCCESS"):
        print 'Build completed successfully!'
    else:
        print 'Build completed with failure'

if argv[0]=='console_logs':
    
    z=console_logs(argv[2])
