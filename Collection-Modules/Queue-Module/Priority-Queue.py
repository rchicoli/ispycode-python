
import Queue

q = Queue.PriorityQueue()

q.put((20, "second"))
q.put((10, "first"))
q.put((30, "third"))

print(q.get())
print(q.get())
print(q.get())


