
import time

year,mon,mday,hour,min,sec,wday,yday,isdst = time.localtime()

print("%s/%s/%s" % (mon,mday,year))
print("%s:%s:%s" % (hour,min,sec))


