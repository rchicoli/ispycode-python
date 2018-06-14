
import Queue

q = Queue.Queue()

q.put(1)
q.put(2)

try:
  print(q.get_nowait())
  print(q.get_nowait())
  print(q.get_nowait())
except Queue.Empty:
  print("the queue is empty")


