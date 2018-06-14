
from datetime import datetime
import pytz

utc = pytz.timezone("UTC")

dt = datetime(2016,12,8,12,55,59,0,utc)
print(dt)

print(dt.tzinfo)


