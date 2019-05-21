import time

def follow(thefile):
    thefile.seek(0,2) # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        yield line

def grep(pattern,lines):
    for line in lines:
        if pattern in line:
            yield line

# Set up a processing pipe : tail -f | grep python
logfile = open("access-log")
loglines = follow(logfile)
pylines = grep("python",loglines)
# Pull results out of the processing pipeline

#for line in pylines:
#    print line,

pylines.next()
print('came here')

g = grep('python')

g.send('abcd')
g.send('python')