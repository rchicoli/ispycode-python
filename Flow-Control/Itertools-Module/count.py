
import itertools

result = itertools.count(0, 10)

for value in result:
  print(value)
  if value <= 100:
    break


