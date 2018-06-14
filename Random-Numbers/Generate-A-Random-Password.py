
import string
import random

def randomPassword():
  minlength=6
  maxlength=12
  length = random.randint(minlength,maxlength)
  letters = string.ascii_letters+string.digits
  return ''.join([random.choice(letters) for _ in range(length)])

password = randomPassword()
print(password)


