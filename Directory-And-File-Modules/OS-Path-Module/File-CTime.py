
import os 
import datetime

# most recent metadata change on Unix, 
# creation time on Windows
t = os.stat('example.py').st_ctime

# print in a date and time
print(datetime.datetime.fromtimestamp(t))


