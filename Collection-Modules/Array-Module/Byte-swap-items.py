
from array import array

numbers = [1,2,3,4]

a = array('i',numbers)
print(a)

a.byteswap()
print(a)


