class Point:
  Z = 0
  def __init__(self, x, y): # constructor
    self.x = x
    self.y = y
  def move(self): # function in class => method
    self.x += 1
    self.y += 1
    print("move")

point = Point(2, 3)
point.move()
print("point:", point.x, point.y, Point.Z)
point.x = 7 # without encap
print("point:", point.x, point.y, Point.Z)


# encapsulate
class Computer:
 def __init__(self):
   self.__maxprice = 900
 def sell(self):
   print('Selling Price: {}'.format(self.__maxprice))
 def setMaxPrice(self, price):
   self.__maxprice = price

c = Computer()
c.sell()

# change the price - show encap data (cannot be changed directly)
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


# Inheritance
class Pet:
  def walk(self):
    print("walk")

class Dog(Pet):
  def bark(self):
    print("woof")
    
dog = Dog()
dog.walk()
dog.bark()
