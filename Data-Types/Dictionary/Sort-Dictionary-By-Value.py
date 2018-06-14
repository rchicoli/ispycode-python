
import operator

# create a dictionary
dict = {'key1':'ccc', 'key2':'bbb', 'key3':'aaa'}
print(dict)

# Sort dictionary by value
sorted_list = sorted(dict.items(), key=operator.itemgetter(1))
for pair in sorted_list:
   print(pair[0], pair[1])


