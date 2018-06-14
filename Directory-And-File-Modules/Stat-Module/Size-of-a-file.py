
import os
import stat

st = os.stat('example.py')

print(st[stat.ST_SIZE])


