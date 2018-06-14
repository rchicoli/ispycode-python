
import time

t = (2016,8,17,20,59,55,2,230,1)

s = time.mktime(t)

print(time.asctime(time.localtime(s)))


