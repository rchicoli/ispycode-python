
import time

t = (2016,8,17,20,59,55,2,230,1)

format = "%b %d %Y"
print(time.strftime(format,t))

format = "%A %B %d %Y %Z"
print(time.strftime(format,t))

format = "%I:%M:%S %p"
print(time.strftime(format,t))


