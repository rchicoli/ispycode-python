
from datetime import time
import pytz

utc = pytz.timezone("UTC")

t = time(11,59,15,123456,utc)
print(t)

print(t.tzinfo)


