
import itertools

values = [1,2,3,4]

result = itertools.permutations(values, 4)
for value in result:
    print(value)


