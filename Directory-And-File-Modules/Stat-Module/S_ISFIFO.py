
import os
import stat

st = os.stat('/run/systemd/initctl/fifo')

if stat.S_ISFIFO(st[stat.ST_MODE]):
   print "FIFO (named pipe)"


