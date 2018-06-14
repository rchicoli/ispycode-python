
from datetime import date

d = date.today()

format = "%b %d %Y"
print(d.strftime(format))

format = "%A %b/%d/%Y"
print(d.strftime(format))


