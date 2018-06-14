
import os
import stat

st = os.stat('/proc/1739/fd/11')

if stat.S_ISSOCK(st[stat.ST_MODE]):
   print "socket"


