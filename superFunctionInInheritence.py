#super class in inheritence using python
class Animal:
  def eat(self):
    print("I can eat")

class Dog(Animal):
  def eat(self):
    super().eat()
    print("I can eat with fruits")
lab = Dog()
lab.eat()
