
import UserList

class MyList(UserList.UserList):

  def __setitem__(self, i, item):
    if i == len(self.data):
      self.data.append(item)
    else:
      self.data[i] = item

list = MyList()

for i in range(10):
  list[i] = i

print list


