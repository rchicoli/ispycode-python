
import itertools

values = [1, 5, 6, 8, 10, 11, 7, 12, 2]

# take values until one is higher than 10.
result = itertools.takewhile(lambda v: v < 11, values)

for value in result:
    print(value)


