
import os
import stat

st = os.stat('/dev/tty')

if stat.S_ISCHR(st[stat.ST_MODE]):
   print "character special device"


