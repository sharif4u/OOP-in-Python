#Use of Inheritance in Python
#base class or parrent class
class Animal:
  def eat(self):
    print("I can eat")
  
  def sleep(sleep):
    print("I can sleep")
#drived or child class
class Dog(Animal):
  def bark(self):
    print("I can bark, woof woof!")
#create a object of Dog drived class
dog1 = Dog()

#call the parrent class members
dog1.eat()
dog1.sleep()

#call the chiled class memebers
dog1.bark()
