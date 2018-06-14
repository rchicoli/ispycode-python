
from datetime import date

d = date.today()
print(d)

d = d.replace(year=2000)
print(d)

d = d.replace(month=12)
print(d)

d = d.replace(day=25)
print(d)


