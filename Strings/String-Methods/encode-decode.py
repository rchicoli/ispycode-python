
str1 = "Hello World"
print(str1)

str2 = str1.encode(encoding='base64',errors='strict')
print(str2)

str3 = str2.decode(encoding='base64',errors='strict')
print(str3)


