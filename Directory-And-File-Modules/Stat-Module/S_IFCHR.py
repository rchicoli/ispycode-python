
import os
import stat

st = os.stat('/dev/tty')
mode = st[stat.ST_MODE]

if mode & stat.S_IFCHR == stat.S_IFCHR:
  print "Character"
else:
  print "NOT"


