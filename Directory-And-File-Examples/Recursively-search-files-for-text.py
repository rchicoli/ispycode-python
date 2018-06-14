
import os

def findtext(dir,phrase):
  for file in os.listdir(dir):
    path = dir + "/" + file
    if os.path.isdir(path):
      findtext(path, phrase)
    else:
      if phrase in open(path).read():
        print(path)

findtext("/var/www/html", "Hello World")


