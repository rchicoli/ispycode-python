
import os
import stat

st = os.stat('/var/log/syslog')
print(st[stat.ST_GID])


