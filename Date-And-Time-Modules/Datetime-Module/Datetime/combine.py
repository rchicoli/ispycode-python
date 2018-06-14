
from datetime import datetime
from datetime import date
from datetime import time

t = time()
print(t)

d = date.today()
print(d)

dt = datetime.combine(d,t)
print(dt)


