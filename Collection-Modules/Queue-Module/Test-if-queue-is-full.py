
import Queue

q = Queue.Queue(2)

q.put(1)
print(q.full())

q.put(2)
print(q.full())


