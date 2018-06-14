
def counting_sort(a, min, max):
    cnt = [0] * (max - min + 1)
    for x in a:
        cnt[x - min] += 1

    return [x for x, n in enumerate(cnt, start=min)
              for i in xrange(n)]

numbers = [2,4,6,8,10,9,7,5,3,1]
print(numbers)

numbers = counting_sort(numbers,1,10)
print(numbers)


