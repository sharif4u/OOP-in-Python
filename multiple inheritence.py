#python multiple inheritence

# a super class
class Animal:
  def Dog(self):
    print(" I am a dog")

#another super class
class Fruit:
  def Mango(self):
    print(" I am a Mango")

#subclass of two class
class Bat(Animal, Fruit):
  pass

#create a boject
b1 = Bat()
b1.Mango()
b1.Dog()

