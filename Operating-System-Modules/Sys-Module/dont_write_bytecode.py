import sys

print(sys.dont_write_bytecode)

sys.dont_write_bytecode = True
print(sys.dont_write_bytecode)


