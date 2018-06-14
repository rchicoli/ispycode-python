
import errno

try:
  f =  open("/tmp/no-such-file", "r")

except Exception, e:
  print(e.errno)
  print(errno.errorcode[e.errno])
  print(e.strerror)


