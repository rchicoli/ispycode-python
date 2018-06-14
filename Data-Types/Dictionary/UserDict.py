
import UserDict

class MyDict(UserDict.UserDict):

  def __init__(self, data = {}, **kw):
    UserDict.UserDict.__init__(self)
    self.update(data)
    self.update(kw)

  def __add__(self, other):
    dict = MyDict(self.data)
    dict.update(b)
    return dict

a = MyDict(a = 1)
b = MyDict(b = 2)

print(a + b)


