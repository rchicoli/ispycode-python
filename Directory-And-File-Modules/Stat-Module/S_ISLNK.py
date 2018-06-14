
import os
import stat

st = os.lstat('/vmlinuz')

if stat.S_ISLNK(st[stat.ST_MODE]):
   print "symbolic link"


