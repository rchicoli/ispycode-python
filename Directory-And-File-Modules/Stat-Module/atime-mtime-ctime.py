
import os
import stat
import time

st = os.stat('example.py')

print "last accessed:", time.ctime(st[stat.ST_ATIME])
print "last modified:", time.ctime(st[stat.ST_MTIME])
print "inode changed:", time.ctime(st[stat.ST_CTIME])


