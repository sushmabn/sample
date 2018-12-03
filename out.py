
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
output = console_logs()    
file = open("sample.txt","w")
file.write(output)
file.close()
