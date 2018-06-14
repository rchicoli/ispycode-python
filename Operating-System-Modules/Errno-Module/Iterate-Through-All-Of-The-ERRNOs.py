
import errno
import os

for i in errno.errorcode.keys():
  print("%s - %s - %s" % (i,errno.errorcode[i],os.strerror(i)))


