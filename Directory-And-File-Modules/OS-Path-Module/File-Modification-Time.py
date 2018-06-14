
import os
import datetime

# Time of most recent content modification expressed in seconds.
t = os.stat('example.py').st_mtime

# print in a date and time
print(datetime.datetime.fromtimestamp(t))


