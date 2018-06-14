
import time
import os

os.environ['TZ'] = 'US/Eastern'
time.tzset()
print(time.tzname)

os.environ['TZ'] = 'Europe/Berlin'
time.tzset()
print(time.tzname)

os.environ['TZ'] = 'Egypt'
time.tzset()
print(time.tzname)


