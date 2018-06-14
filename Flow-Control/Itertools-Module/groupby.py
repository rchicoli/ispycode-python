
import itertools
import operator

things = [('A', 1),
          ('A', 2),
          ('B', 3),
          ('B', 4),
          ('C', 5),
          ('C', 6)]

for key, items in itertools.groupby(things, operator.itemgetter(0)):
  print(key)
  for item in items:
    print(item)


