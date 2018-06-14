
from array import *

s = open("/tmp/file.txt", 'r').read()
chars = array('c',list(s))

for c in chars:
   print(type(c))


