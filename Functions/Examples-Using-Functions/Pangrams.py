
import string, sys
def is_pangram(str1, alphabet=string.ascii_lowercase):
  alphaset = set(alphabet)  
  return alphaset <= set(str1.lower())  

var = is_pangram('The quick brown fox jumps over the lazy dog')
print(var)


