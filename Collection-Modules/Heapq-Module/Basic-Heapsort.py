
import heapq

def heapsort(iterable):
  h = []
  for value in iterable:
    heapq.heappush(h, value)
  return [heapq.heappop(h) for i in range(len(h))]

unsorted = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(unsorted)

sorted = heapsort(unsorted)
print(sorted)


