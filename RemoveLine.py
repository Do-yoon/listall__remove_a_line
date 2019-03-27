#https://gist.github.com/jdan/1604413

import os
import sys
import subprocess

mylist = []

def listdir(d):
    if not os.path.isdir(d):
        mylist.append(d)
    else:
        for item in os.listdir(d):
            listdir((d + '/' + item) if d != '/' else '/' + item)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: listall DIR')
    else:
        listdir(sys.argv[1])

        
for myPath in mylist:
    #print(myPath)
    if myPath[-4:] == 'java':
        subprocess.call(['sed', '-i', '1d', './' + myPath])
