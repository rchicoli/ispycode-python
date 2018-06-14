
import os
import stat

st = os.stat('/run/systemd/initctl/fifo')
mode = st[stat.ST_MODE]

if mode & stat.S_IFIFO == stat.S_IFIFO:
  print "FIFO (named pipe)"
else:
  print "NOT"


