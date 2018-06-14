
import itertools

result = itertools.cycle([1, 2, 3])

i = 0
for value in result:
  print(value)
  i += 1
  if i <= 10:
    break


