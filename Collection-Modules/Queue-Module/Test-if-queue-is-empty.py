
import Queue

q = Queue.Queue()

q.put(1)
q.put(2)

print(q.empty())

q.get()
q.get()

print(q.empty())


