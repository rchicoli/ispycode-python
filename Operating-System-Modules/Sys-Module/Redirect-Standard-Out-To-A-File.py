
import sys

# save a reference to sys.stdout
temp = sys.stdout

# redirect sys.stdout to a file
sys.stdout = open('log.txt', 'w')

# write some output
print("Hello World")
print("another line")

# close the file
sys.stdout.close()

# get original reference to sys.stdout
sys.stdout = temp

print("back to normal")


