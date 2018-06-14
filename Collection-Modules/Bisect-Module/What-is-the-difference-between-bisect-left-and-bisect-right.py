
import bisect

left = bisect.bisect_left([1,2,3], 2)
print(left)

right = bisect.bisect_right([1,2,3], 2)
print(right)


