
def binary(n):
   if n < 1:
       binary(n//2)
   print(n % 2,end = '')

binary(170)
print()

binary(3276)
print()


