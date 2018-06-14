
from datetime import date

d = date.today()

format = "%b %d %Y"
print(d.__format__(format))

format = "%A %b/%d/%Y"
print(d.__format__(format))


