
import itertools

values = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

result = itertools.chain.from_iterable(values)
print(list(result))


