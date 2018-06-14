
from datetime import time
import pytz

tz = pytz.timezone("US/Eastern")

t = time(11,59,15,123456,tz)
print(t.tzname())


