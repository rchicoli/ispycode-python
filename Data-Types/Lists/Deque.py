
from collections import deque

queue = deque([]);
print(queue)

queue.append('a')
print(queue)

queue.append('b')
print(queue)

char = queue.popleft()
print(queue)

queue.append('c')
print(queue)

char = queue.popleft()
print(queue)

char = queue.popleft()
print(queue)


