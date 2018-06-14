
import shutil

file1 = open('file1.txt')
file2 = open('file2.txt', 'a')

shutil.copyfileobj(file1, file2, 1024)

file1.close()
file2.close()


