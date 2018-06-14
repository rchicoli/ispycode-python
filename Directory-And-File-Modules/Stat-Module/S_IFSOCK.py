
import os
import stat

st = os.stat('/proc/1739/fd/11')
mode = st[stat.ST_MODE]

if mode & stat.S_IFSOCK == stat.S_IFSOCK:
  print("Socket")
else:
  print("NOT")


