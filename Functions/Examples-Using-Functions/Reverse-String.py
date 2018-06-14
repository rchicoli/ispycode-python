
def reverse_string(str):
    rstr = ''
    index = len(str)
    while index > 0:
        rstr += str[ index - 1 ]
        index = index - 1
    return rstr

old_string = 'abcdefg'
new_string = reverse_string(old_string)

print(old_string)
print(new_string)


