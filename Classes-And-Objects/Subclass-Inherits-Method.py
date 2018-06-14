
class Pet:
  sound = "none"
  def speak(self):
    print(self.sound)

class Dog(Pet):
  sound = "bark"


p = Pet()
p.speak()

d = Dog()
d.speak()


