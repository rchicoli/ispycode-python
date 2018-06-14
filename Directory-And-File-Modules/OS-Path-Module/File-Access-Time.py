
import os
import datetime

# Time of most recent access expressed in seconds
t = os.stat('example.py').st_atime

# print in a date and time
print(datetime.datetime.fromtimestamp(t))


