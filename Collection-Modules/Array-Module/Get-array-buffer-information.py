
from array import array

numbers = [1,2,3,4]

a = array('i',numbers)
print(a)

t = a.buffer_info()
print(t)


