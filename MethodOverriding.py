#method Overriding
class Animal:
  name = ""
  def eat(self):
    print("I can eat")

class Dog(Animal):
  def eat(self):
    print("I can eat with fruit's")

labrador = Dog()

labrador.eat()
