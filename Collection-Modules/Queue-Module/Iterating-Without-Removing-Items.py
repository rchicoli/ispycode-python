
import Queue

q = Queue.Queue()

q.put('a')
q.put('b')
q.put('c')

for elem in list(q.queue):
  print(elem)

print("Size: %s" % q.qsize())


