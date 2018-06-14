
def cocktail_sort(A):
  up = range(len(A)-1)
  while True:
    for indices in (up, reversed(up)):
      swapped = False
      for i in indices:
        if A[i] > A[i+1]:
          A[i], A[i+1] =  A[i+1], A[i]
          swapped = True
      if not swapped:
        return

numbers = [2,4,6,8,10,9,7,5,3,1]
print(numbers)

cocktail_sort(numbers)
print(numbers)


