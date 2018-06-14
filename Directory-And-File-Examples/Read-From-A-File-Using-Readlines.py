
from __future__ import print_function

f = open('colors.txt', 'r')
output = f.readlines()
f.close()

for line in output:
  print(line,  end="")


