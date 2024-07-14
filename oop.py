# class Student:

#   def __init__(self, name, age, grade):
#       self.name = name
#       self.age = age
#       self.grade = grade

#   def get_grade(self):
#       return self.grade

# class Course:

#   def __init__(self, name, max_students):
#       self.name = name
#       self.max_students = max_students
#       self.students = []
  
#   def add_student(self, student):
#       if len(self.students) < self.max_students:
#         self.students.append(student)
#         return True
#       return False
  
#   def get_average_grade(self):
#       value = 0
#       for student in self.students:
#          value += student.get_grade()

#       return value / len(self.students)

# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)

# course = Course("Scienece", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.get_average_grade())

# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")
    
#     def speak(self):
#         print("I don't know what I say")

# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     def speak(self):
#         print("Meow")
    
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

# class Dog(Pet):
#       def speak(self):
#           print("Bark")

# p = Pet("Time", 19)
# p.speak()

# c = Cat("Bill", 34)
# c.show()

# d = Dog("Jill", 25)
# d.speak()

# class Person:
#     number_of_people = 0
#     GRAVITY = -9.8

#     def __init__(self, name):
#         self.name = name
#         Person.add_person()
    
#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people

#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1

# p1 = Person("tim")
# p2 = Person("jill")

# Person.number_of_people = 8
# print(Person.number_of_people_())

# class Math:

#   @staticmethod
#   def add5(x):
#       return x + 5

#   @staticmethod
#   def add10(x):
#       return x + 10

#   @staticmethod
#   def pr():
#       print("run")

# print(Math.pr())

# from math import pi

# class Circle:
#     # A Circle instance models a circle with a radius

#     def __init__(self, radius=1.0):
#         # Initializer with default of 1.0
#         self.radius = radius

#     def __str__(self):
#         # Return a description string for this instance, invoked by print and str()  
#         return "This is a circle with radius of {:.2f}".format(self.radius)

#     def __repr__(self):
#         # Return a formal string that can be used to re-create this instance, invoked repr()
#         return "Circle(radius={})".format(self.radius)

#     def get_area(self):
#         # Return the area of this cricle instance
#         return self.radius * self.radius * pi

# class Cylinder(Circle):
#     # "The Cylinder class is a sublcass of Circle"

#     def __init__(self, radius = 1.0, height = 1.0):
#         # "Initializer"
#         super().__init__(radius)
#         # OR
#         # super(Cylinder, self).__init__(radius) (Python 2)
#         # Circle.__init__(self, radius)          Explicit superclass class
#         self.height = height

#     def __str__(self):
#         # "Self Description for print() and str()"
#         # If __str__ is missing in the subclass, print() will invoke the superclass version!
#         return "Cylinder(radius={},height={})".format(self.radius, self.height)

#     def get_volume(self):
#         "Return the volume of the cyclinder"
#         return self.get_area() * self.height # Inherited get_area()
    
# c1 = Circle(2.1) # Construct an instance

# print(c1) # Invoke __str__(): This is a circle with radius of 2.10
# print(c1.get_area()) # 13.854423602330987
# print(c1.radius) # 2.1

# print(str(c1)) # Invoice __str__(): This is a circle with radius of 2.10
# print(repr(c1)) # Invoke __repr__(): Circle(radius=2.1)
    
# cy1 = Cylinder(1.1, 2.2)

# print(cy1) # Invoke __str__()
# print(cy1.get_area()) # User superclass method
# print(cy1.get_volume()) # Invoke its method
# print(cy1.radius)
# print(cy1.height)

# cy2 = Cylinder()
# print(cy2)
# print(cy2.get_area())
# print(cy2.get_volume())
# print(dir(cy1))

# print(Cylinder.get_area)
    
# c1 = Circle(3.3)
# print(c1) # Output: This is a circle with radius of 3.30

# print(isinstance(c1, Circle)) # True
# print(isinstance(c1, Cylinder)) # False (A superclass object is Not a subclass object)

# class MyClass:
    
#     @classmethod
#     def hello(self, name):
#         print(self)
#         print("Hello from", self.__name__,",",name)

# MyClass.hello("Vincent")

# class MyClass:

#   def hello(self):
#     print("Hello from", self.__class__.__name__)

# MyClass().hello()
    
# 1. Single Inheritance
    
# class Country:
#     def ShowCountry(self):
#         print("This is India")

# class State(Country):
#     def ShowState(self):
#         print("This is State")

# st = State()
# st.ShowCountry()
# st.ShowState()

# 2. Multiple Inheritance

# When derived class contains more than 1 base class is called Multiple inheritance

# class student:
#     def method1(self, sno, sname):
#         self.sno = sno
#         self.sname = sname
    
#     def method2(self):
#         print("Student No : ", self.sno)
#         print("Student No : ", self.sname)

# class marks:
#     def setmarks(self, m1, m2):
#         self.mark1 = m1
#         self.mark2 = m2
    
#     def putmarks(self):
#         print("Mark1 : ", self.mark1)
#         print("Mark2 : ", self.mark2)

# class result(marks, student): # multiple inheritance
#     def calc(self):
#         self.total = self.mark1 + self.mark2
    
#     def puttotal(self):
#         print("Total : ", self.total)

# r = result()

# r.method1(60, "Lucky")
# r.setmarks(50,60)
# r.calc()
# r.method2()
# r.putmarks()
# r.puttotal()

# 3. Multilevel Inheritance

# A derived class derived from base class which is again dervied from class

# A->B->C->D->E

# class student:
#     def setstud(self, sno, sname):
#         self.sno = sno;
#         self.sname = sname;

#     def putstud(self):
#         print("Student No : ",self.sno)
#         print("Student Name : ",self.sname)

# class marks(student):
#     def setmarks(self, m1, m2):
#         self.mark1 = m1
#         self.mark2 = m2
    
#     def putmarks(self):
#         print("Mark1 : ", self.mark1)
#         print("Mark2 : ", self.mark2)

# class result(marks):
#     def calc(self):
#         self.total = self.mark1 + self.mark2
    
#     def puttotal(self):
#         print("Total : ", self.total)

# r = result()
# r.setstud(60, "Mahesh")
# r.setmarks(50, 60)
# r.calc()
# r.putstud()
# r.putmarks()
# r.puttotal()

# 4. Hierarchal Inheritance

# A one base class contains more than one dervied class.

# father -> child and child 2

# class one:
#     def display(self):
#         self.x=1000
#         self.y=2000
#         print("This is the method in class one")
#         print("Value of X= ",self.x)
#         print("Value of Y= ",self.y)

# class two(one):
#     def add(self):
#         print("This is the method in class two")
#         print("X+Y= ",(self.x+self.y))

# class three(one):
#     def mul(self):
#         print("This is the method in class three")
#         print("X*Y= ",(self.x*self.y))

# t1=two()
# t2=three()

# t1.display()
# t2.display()

# t1.add()
# t2.mul()
    
# 5. Hybird Inheritance
# Combination of multiple + multilevel inheritance

# class student:
#     def setstud(self, sno, sname):
#         self.sno = sno
#         self.sname = sname
    
#     def putstud(self):
#         print("Student No : ", self.sno)
#         print("Student Name : ", self.sname)

# class marks(student):
#     def setmarks(self, m1, m2):
#         self.mark1 = m1;
#         self.mark2 = m2;

#     def putmarks(self):
#         print("Mark1 : ", self.mark1);
#         print("Mark2 : ", self.mark2)

# class practical:
#     def getpractical(self, p1):
#         self.p1=p1
    
#     def putpractical(self):
#         print("Practical mark=",self.p1)

# class result(marks, practical):
#     def calc(self):
#         self.total = self.mark1 + self.mark2 + self.p1
    
#     def puttotal(self):
#         print("Total : ", self.total)

# r = result()

# r.setstud(60, "Ash")
# r.setmarks(50, 60)
# r.getpractical(100)
# r.calc()
# r.putstud()
# r.putmarks()
# r.putpractical()
# r.puttotal()

# Polymorphism

# The term polymorphism, in the OOP language, refers to the ability of an object to adapt the code to the type of the data it is processing.

# In python polymorphism is one of the key concepts, and we can say that it is a built-in feature

# Example 1: Polymorphism in addition operator We know that the + operator is used extensively in Python programs. But, it does not have a single usage

# For integer data types, + operator

# is used to perform arithmetic addition operation
# for string data types, + operator to perform concatenation
  
# num1 = 1
# num2 = 2
# print(num1+num2)

# str1 = "Python"
# str2 = "Programming"
# print(str1+" "+str2)

# Here, we can see that a single operator + has been used to carry out different operations for distinct data types.
# Is one of the most simple occurences of polymorphism in Python.


# 1. Polymorphism through method overloading

  # -Method overloading in its tradional sense, where you can have more than one method having 
  # the same name with in the class where the methods differ in types or number of arguments passed,
  # is not supported in Python.

  # -Trying to have methods with same name wont result in compile time error in Python but only the
  # last defined method is recognized in such scenario, calling any other overloaded function results
  # in an error.

  # -But you can still simulate polymorphism through method overloading by using default arguments
  # in a method.

    # In the example there is 1 default argument in the method sum.
    # If the method called with 2 parameters for the 3rd default value is used.
    # If the method called with 3 parameters passed value is used for the 3rd parameter.

# class OverloadDemo:
#   # sum method with one default parameter
#   def sum(self, a, b, c=0):
#       s = a + b + c
#       return s

# od = OverloadDemo()

# # Calling method with 2 args
# sum = od.sum(7, 8)
# print("Sum is : ", sum)

# # Calling method with 3 args
# sum = od.sum(7, 8, 9)
# print("Sum is : ", sum)

# 2. Polymorphism through inheritance- Method overriding
  
#   Method overriding provides ability to change the implementation of a method in a child
#   class which is already defined in one of its super class.

#   If there is a method in a super class and method having the same name and same number of 
#   arguments in a child class then the child class method is said to be overriding the parent class
#   method.

#   calling methods

#     When the method is called with parent class object, method of the parent class is executed.
#     When method is called with child class object. method of the child class is executed.

#   So the appropriate overriden method is called based on the object type, which is an example of
#   Polymorphism.

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
  
#     def displayData(self):
#         print("In parent class displayData method")
#         print(self.name)
#         print(self.age)

# class Employee(Person):
   
#     def __init__(self, name, age, id):
#         # calling constructor of super class
#         super().__init__(name, age)
#         self.empId = id
  
#     def displayData(self):
#         print("In child class displayData method")
#         print(self.name)
#         print(self.age)
#         print(self.empId)

# # Person class object
# person = Person("John", 40)
# person.displayData()

# # Employee class object
# emp = Employee("John", 40, "E005")
# emp.displayData()

# 3. Polymorphism through `oeprator overloading

    # Operator overloading means the ability to overload the operator to provide extra functionality
    # in addition to its real operational meaning.

      # Operator overloading is also an example of polymorphism as the same operator can perform
      # different actions.

    # For example "+" operator which is used with numbers to perform addition operation. But "+" operator
    # when used with two strings concatenate those Strings and merge two lists when used with lists in Python.

  # When is Operator overloading required

    # In the above example "+" operator worked with Strings and Lists because it is already overloaded
    # to provide the functionality for String and List.

    # What if you want to use operator with custom objects.

    # For example if you want to use "+" operator with your custom class objects.

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p1 = Point(1, 2)
# p2 = Point(3, 4)

# print(p1+p2)

# As you can see trying to add two objects results in an error "unsupported operand type(s) for +"
# because "+" operator doesnt know how to add these two objects.

# What we want to do here is to add the data (p1.x + p2.x) and (p1.y + p2.y) of these two objects but that
# will require operator overloading as that is some extra functionality that you want "+" operator to perform.

# For all operators internally Python defines methods to provide functionality for those operators.

#   For example functionality for "+" operator is provide by special method add().
#   Whenever "+" operator is used internally add() method is invoked to do the operation.

# Internal methods that provide functionality for the operators are known as magic methiods in
# Python.

# These magic methods are automatically invoked when corresponding operators are used.

# When we want any operator to work with custom objects you need to override the corresponding
# special method that proveds functionality for the operator.
   
# In the example there is a class Point with two variables x and y. Two object of Point class are
# instantiated and you try to add those objects with the intention to add the data (p1.x + p2.x) and
# (p1.y + p2.y) of these two objects.

# In order to successfully do that magic method __add__() has to be overridden in your class to 
# provide that functionality.

# class Point:
     
#      def __init__(self, x, y):
#          self.x = x
#          self.y = y

#      def __add__(self, other):
#          return self.x + other.x, self.y + other.y

# p1 = Point(1, 2)
# p2 = Point(3, 4) 

# print(p1+p2)

# Magic methods in Python are the methods prefixed with two underscores and suffixed with two underscores.
#   These magic methods are also known as Dunders (Double UNDERscores) in Python.

# Magic methods for arithmetic operators

  # Operator || Magic Method ||             Description

  # +           __add__(self, other)        Additive operator
  # -           __sub__(self, other)        Subtraction operator
  # *           __mul__(self, other)        Multiplication operator
  # /           __truediv__(self, other)    Division with fractional result
  # %           __mod__(self, other)        Remainder operator
  # //          __floordiv__(self, other)   Division with integer result, dscarding any fractional part
  # **          __pow__(self, other)        Return a to the power b, for a and b numbers
  # @           __matmul__(self, other)     Matrix Multiplication. Available from version 3.5

# Magic methods for Comparison operators

# Operator || Magic Method ||            Description

  # <         __lt__(self, other)        less than
  # <=        __le__(self, other)        less than or equal to
  # ==        __eq__(self, other)        equal to
  # !=        __ne__(self, other)        not equal to

# Magic methods for unary operators

# Operator || Magic Method ||            Description

  # +        pos(self, other)            Unary plus operator, indicates positive value
  # -        neg(self, other)            Unary minus operator, negates an experession
  # ~        invert(self, other)         Returns the bitwise inverse of the number

# Example : Overloading "*" operator in Python

# class Point:
    
#     def __init__(self, x):
#         self.x = x
    
#     #overriding magic method
#     def __mul__(self, other):
#         return self.x * other.x

# p1 = Point(12)
# p2 = Point(5)

# print(p1*p2)

# Example: Overloading comparison operator (>)

# class Person:
    
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     #overriding magic method
#     def __gt__(self, other):
#         return self.salary > other.salary

# obj1 = Person("John", 4500)
# obj2 = Person("Natasha", 6000)

# print(obj1.name, "earns more than", obj2.name, "-", obj1 > obj2)

# STACK - Abstract Data Structure - implementation using basic python + OOP

# The name Stack data structure resembles a pile of objects, stack of papers, or a tower of blocks, where
# adding and removing of items occur only at the top of the pile.

# A stack an abstract linear data type, collection of objects that supports fast last-in, first-out (LIFO)
# semantics for inserts and deletes.

# Unlike lists or arrays, stacks typically dont allow for random access to the objects they contain.

# The insert and delete operations are also often called push and pop

# Stacks and Queues are both linear collections of items.

#   However, in a queue, the least recently added item is removed first, following the first in first out or FIFO manner.

#   On the other hand, in a stack, the most recently added items is removed in the beginning following the LIFO.

# A real-life example of a stack is a pile of heavy and precious plates, all kept on top of the other. If you wish to add a plat or remove one,
# you can do that only from the top. However, if you want to remove a lower plate from the stack, you have to remove the topmost plates one by one,
# in order to

  # A useful real-world analogy for a stack data structure is a stack of plates:
  #   New plates are added to the top of the stack. And because the plates are precious and heavy, only the topmost plate
  #   can be moved (last-in, first-out). To reach the plates lower down in the stack the topmost plates must be removed
  #   one by one.

# The basic operations which are performed in the stack are mentioned below:

#   Push: Adds an item in the stack. Once the stack is full, it is said to be in an Overflow Condition.
#   Pop: Removes an item from the stack. It follows a reversed order to pop items similar to the way when items are
#   pushed. It is said to be an underflow condition.
#   Peek or Top: Returns top element of stack.
#   isEmpty: Returns true if stack is empty, else false.

# Application of Stack

#   They are used to reverse a string. Each of the characters are pushed in and then popped off, which results in a
#   reversed string.
#   It is used in Expression Evaluation and Expression Conversion (Infix to postfix, infix to prefix, postfix to 
#   infix, prefix to infix). 
#   It is used for forward and backward features in web browsers.
#   It is used for recursive parsing in Natural Language Processing.
#   It is used in syntax parsing and parenthesis checking.
#   It is used for Backtracking like finding paths to a maze or exhaustive searching
#   It is used in Algorythms like Tower of Hanoi, tree traversals, histogram problem and also in graph algorithms
#   like Topological Sorting

# Understanding Stack Operations
    
# There are mainly two types of primitive stack operations:

# Push: It is performed to insert and store an element in the stack. However, when you try to insert an element in a stack
#       which is full, the Overflow condition occurs.
# Pop: It is used to remove an element from the stack. However, when the stack is empty, the underflow condition occurs.

# Push: lets consider editing a python file using the undo feature in your editor so you can have a clear understanding of
# the stack operations. At first, a new function called Insert is added. The push operation adds the Insert function into the stack:

# Implementing Stack in Pythong

  # Python gives a lot of options for implementing a Python stack. However, there are some basic implementations of
  # Python stack that will fulfill most of your needs.

  # Some of those implementations are as follows:

  #   using list
  #   using collections.deque
  #   using custom method (of course ! we are going to do a toy implementation in this project!)
  #   numerous 3rd party packages

# Option 1 - The list Built-in

  # Python's built-in list type makes a decent stack data structure as it supports push and pop operations in amortized
  # O(1) time

# define a stack
# s = []

# add some items to it
# s.append("eat")
# s.append("sleep")
# s.append("code")

# print the stack
# print(s)
# ["eat", "sleep", "code"]
# s.pop()
# s.pop()
# s.pop()

# print(s)

# Option 2 - The list Built-in

  # Using collections.deque
  # Python contains a module named collections. This comprises of the deque class which is a double-ended queue
  # that supports inserting and removing elements from either ends.
  # Because deques support adding and removing elements from either and equally well, they can serve both a queues
  # and as stacks.

# The method of deque is similar to the lists.

# from collections import deque
# q = deque()

# q.append("eat")
# q.append("sleep")
# q.append("code")

# q.pop()
# q.pop()
# q.pop()

# Option 3 - Custom method useing classes/objects

# The following stack implementation assumes that the end of the list will hold the top element of the stack.
# As the stack grows (as push operations occur), new items will be added on the end of the list
# pop operations will manipulate that same end

# define stack class
class StackTOPn:
    def __init__(self):
        self.items = []
    
    # for printing the stack contents
    def __str__(self):
        return " ".join([str(i) for i in self.items])
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def display_all_items(self):
        return (self.items)

# s = StackTOPn()
# print(s)
# print(s.isEmpty())

# s.push("FIRST")
# s.push("SECOND")
# s.push("THIRD")

# print(s.display_all_items())

# for item in s.display_all_items():
#   print(item)

# Another implementation

# TOP is the beginning of the list (0th element)

# class StackTOP0:
#     def __init__(self):
#         self.items = []
    
#     def isEmpty(self):
#         return self.items == []
    
#     def push(self, item):
#         self.items.insert(0, item)
    
#     def pop(self):
#         return self.items.pop(0)
    
#     def peek(self):
#         return self.items[0]

#     def size(self):
#         return len(self.items)

#     def display_all_items(self):
#         return (self.items)

# stop0 = StackTOP0()
# stop0.isEmpty()

# stop0.push("FIRST")
# stop0.push("SECOND")
# stop0.push("THIRD")

# get the recent item inserted
# print(stop0.peek())

# view the stack
# for item in stop0.display_all_items():
#     print(item)

# Exercise - 3
    
# Write a function revstring(mystr) that uses a stack to reverse the characters in a string

# initiate a stack (TOPn)
myStack = StackTOPn()

input_string = "bangalore"

for ch in input_string:
    myStack.push(ch)

# print the stack
# print(myStack.display_all_items())

# get the reverse of the string

rev_string = []
rev_str = ""

while not myStack.isEmpty():

  pop_ch = myStack.pop()

  rev_string.append(pop_ch)
  rev_str = rev_str + pop_ch

print("reverse string is: ", rev_string)
print("reverse string is: ", rev_str)