
import itertools

numbers  = [1,2,3,4,5,6,7,8,9]
booleans = [1,0,1,0,1,0,1,0,1]

result = list(itertools.compress(numbers,booleans))

print(result)


