
import os

# get tupla values of os.uname()
(system, node, release, version, machine) = os.uname()

# print values
print "System: " , system
print "Node: " , node
print "Version: " , version
print "Machine: " , machine


