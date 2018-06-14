
import re

str1 = '1Hello2World3'
print(str1)

str2 = re.sub("[^A-Za-z]", "", str1)
print(str2)


