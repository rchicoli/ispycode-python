
import sys

print("script name is %s" % sys.argv[0])

if len(sys.argv) > 1:
  print("there are %s arguments" % (len(sys.argv)-1) )
  for arg in sys.argv[1:]:
    print arg
else:
  print "there are no arguments"


