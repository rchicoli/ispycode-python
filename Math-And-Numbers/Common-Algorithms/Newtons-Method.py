
def isqrt(n):
  xn = 1
  xn1 = (xn + n/xn)/2
  while abs(xn1 - xn) > 1:
    xn = xn1
    xn1 = (xn + n/xn)/2
  while xn1*xn1 > n:
    xn1 -= 1
  return xn1


results = isqrt(100)
print results

results = isqrt(625)
print results


