
import os
import stat

st = os.stat('file1')
print(st[stat.ST_NLINK])


