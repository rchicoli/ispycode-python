
import itertools

numbers = [1,2,3,4,5,6,7,8,9,10]

result = itertools.filterfalse(lambda x: x%3, numbers)
for i in result:
    print(i)


