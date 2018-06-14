
import Queue

q = Queue.Queue(2)
try:
  q.put_nowait(1)
  q.put_nowait(2)
  q.put_nowait(3)
except Queue.Full:
  print("the queue is full")


