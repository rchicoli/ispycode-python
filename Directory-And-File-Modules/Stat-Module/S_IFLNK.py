
import os
import stat

st = os.lstat('/vmlinuz')
mode = st[stat.ST_MODE]

if mode & stat.S_IFLNK == stat.S_IFLNK:
  print("Symbolic link")
else:
  print("NOT")


