
import os
import stat
from datetime import datetime

st = os.stat('example.py')
print(datetime.fromtimestamp(st[stat.ST_CTIME]))


