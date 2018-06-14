
import os
import stat

st = os.stat('example.py')

if stat.S_ISREG(st[stat.ST_MODE]):
   print "regular file"


