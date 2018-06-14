
import sys

print(sys.getrecursionlimit())

def fun(x):
  try:
    x += 1
    fun(x)
  except:
    print("Recursion count: %s" % x)

fun(1)


