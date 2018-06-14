
import os
import stat

st = os.stat('example.py')
mode = st[stat.ST_MODE]

if mode & stat.S_IFREG == stat.S_IFREG:
  print("Regular")
else:
  print("NOT")


