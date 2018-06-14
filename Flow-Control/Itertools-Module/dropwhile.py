
import itertools

numbers = [1,2,3,4,5,6,7,8,9,10]
result = itertools.dropwhile(lambda i: i<=5, numbers)
for number in result:
    print(number)


