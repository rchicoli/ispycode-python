
import time

print(time.clock())

# waste some cpu cycles
x = 0
while (x < 50000000):
  x += 1

print(time.clock())


