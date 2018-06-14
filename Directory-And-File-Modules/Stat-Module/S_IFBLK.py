
import os
import stat

st = os.stat('/dev/sr0')
mode = st[stat.ST_MODE]

if mode & stat.S_IFBLK == stat.S_IFBLK:
  print("Block")
else:
  print("NOT")


