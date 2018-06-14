
from datetime import timedelta
from datetime import datetime
import time

d1 = datetime.now()
time.sleep(10)
d2 = datetime.now()

delta = d2 - d1
seconds = delta.total_seconds()
print(seconds)


