
import os
import stat

st = os.stat('/')
mode = st[stat.ST_MODE]

if mode & stat.S_IFDIR == stat.S_IFDIR:
  print("Directory")
else:
  print("NOT")


