
from __future__ import print_function

f = open('colors.txt', 'r')
for line in f:
  print(line,  end="")
f.close()


