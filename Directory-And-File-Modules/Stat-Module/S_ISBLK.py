
import os
import stat

st = os.stat('/dev/sr0')

if stat.S_ISBLK(st[stat.ST_MODE]):
   print "block special device"


