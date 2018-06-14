
import itertools

values = [1, 2, 3, 4, 5]

result = itertools.combinations(values,3)
for comb in result:
  print(comb)


