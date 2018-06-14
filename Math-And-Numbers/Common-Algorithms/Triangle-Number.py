
def triangle_numbers(n):
    return [i*(i+1)/2 for i in xrange(n)]


results = triangle_numbers(10)
print(results)


