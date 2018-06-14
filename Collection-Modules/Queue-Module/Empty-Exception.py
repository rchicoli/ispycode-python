
import Queue

q = Queue.Queue()

q.put(1)
q.put(2)

try:
  q.get_nowait()
  q.get_nowait()
  q.get_nowait()
except Queue.Empty:
  print("the queue is empty")


