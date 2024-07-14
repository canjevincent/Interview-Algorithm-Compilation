class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

class Python:
  def __init__(self, name):
    self.name = name

bubba = Python('Bubba')

print(bubba.name)