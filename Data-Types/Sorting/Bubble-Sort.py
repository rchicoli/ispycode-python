
def bubblesort(alist):
  for passnum in range(len(alist)-1,0,-1):
    for i in range(passnum):
      if alist[i]>alist[i+1]:
        temp = alist[i]
        alist[i] = alist[i+1]
        alist[i+1] = temp

numbers = [2,4,6,8,10,9,7,5,3,1]
print(numbers)
bubblesort(numbers)
print(numbers)


