
from datetime import datetime
import pytz

utc = pytz.timezone("UTC")
italy = pytz.timezone("Europe/Rome")

dt1 = datetime(2008, 7, 6, 5, 4, 3, tzinfo=italy)
print(dt1.timetz())

dt2 = dt1.astimezone(utc)
print(dt2.timetz())


