
import itertools

for i in itertools.product('ABC', 'xyz'):
  print(i)

for i in itertools.product([0,1], repeat=3):
  print(i)


