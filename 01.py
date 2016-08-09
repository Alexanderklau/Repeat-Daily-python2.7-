import os
ls = os.linesep

while True:
    if os.path.exists(fname):
        print "Error: '%s' already exists" % fname
    else:
        break

    all = []
    print "\nEnter lines ('. ' by itself to quit).\n"
while True:
    entry = raw_input('> ')
    if entry == '. ':
        break
    else:
        all.append(entry)

fobh = open(fname,'w')
fobh = writelines(['%s%s' % (x,ls) for x in all])
fobh.close()
print 'Done!'