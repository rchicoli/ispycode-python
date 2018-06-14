
import itertools
import operator

numbers = [1,2,3,4,5,6,7,8,9,10]

result = list(itertools.accumulate(numbers,operator.add))
print(result)

result = list(itertools.accumulate(numbers,operator.mul))
print(result)

result = list(itertools.accumulate(numbers,min))
print(result)

result = list(itertools.accumulate(numbers,lambda total,i :total*10 + i ))
print(result)


