
import stat
import time
import os

f = "example.py"
st = os.stat(f)
mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
print("size: %s bytes" % size)
print("owner: %s %s" % (uid,gid) )
print("created: %s" % time.ctime(ctime))
print("last accessed: %s" % time.ctime(atime))
print("last modified: %s" % time.ctime(mtime))
print("mode: %s" % oct(mode))
print("inode/dev: %s %s" % (ino,dev))


