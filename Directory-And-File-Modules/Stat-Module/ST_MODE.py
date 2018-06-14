
import os
import stat

st = os.stat('example.py')
print(oct(st[stat.ST_MODE]))


