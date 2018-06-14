
import os
import stat

st = os.stat('/tmp')

if stat.S_ISDIR(st[stat.ST_MODE]):
   print "directory"


