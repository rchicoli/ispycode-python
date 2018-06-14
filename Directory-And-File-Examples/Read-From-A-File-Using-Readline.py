
from __future__ import print_function

f = open('colors.txt', 'r')
while True:
  line = f.readline()
  if not line:
    break
  print(line,  end="")
f.close()


