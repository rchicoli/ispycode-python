
from datetime import time

t = time(12,45,59)
format = '%H:%M:%S'

str = t.strftime(format)

print(str)


