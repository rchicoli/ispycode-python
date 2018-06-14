
from itertools import tee

data =[1,2,3,4]

iter1, iter2 = tee(data)

print('--iter1--')
for item in iter1:
  print(item)

print('--iter2--')
for item in iter2:
  print(item)


