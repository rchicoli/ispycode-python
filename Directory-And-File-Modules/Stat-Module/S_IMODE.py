
import os
import stat

st = os.stat('example.py')
mode = st[stat.ST_MODE]

print(oct(stat.S_IMODE(mode)))


