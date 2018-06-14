
import time

st = time.struct_time([2016,8,19,10,35,7,4,232,0])

print(type(st))

print(st)

print(st.tm_year)
print(st.tm_mon)
print(st.tm_mday)
print(st.tm_min)
print(st.tm_sec)
print(st.tm_wday)
print(st.tm_yday)
print(st.tm_isdst)


