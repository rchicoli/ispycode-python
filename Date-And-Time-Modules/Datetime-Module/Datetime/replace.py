
from datetime import datetime

dt = datetime.today()
print(dt)

dt = dt.replace(year=2011)
print(dt)

dt = dt.replace(month=11)
print(dt)

dt = dt.replace(day=11)
print(dt)

dt = dt.replace(hour=11)
print(dt)

dt = dt.replace(minute=11)
print(dt)

dt = dt.replace(second=11)
print(dt)

dt = dt.replace(microsecond=111111)
print(dt)


