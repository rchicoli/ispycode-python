
from heapq import merge

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


numbers = [2,4,6,8,10,9,7,5,3,1]
print(numbers)
numbers = merge_sort(numbers)
print(numbers)


