
import heapq

heap = []

# add some values to the heap
for value in [2,4,6,8,1,3,5,7]:
  heapq.heappush(heap, value)

# pop them off, in order
while heap:
  print heapq.heappop(heap),


