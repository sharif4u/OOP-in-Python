#Multilevel Inheritence in python
class Super:
  def info(self):
    print("this is a method of super class")

class Drived:
  def info(self):
    print("this is a method of drived class")

class Drived2(Super, Drived):
  def drivedMethod2(self):
    print("this is a method of super class 2")

drive = Drived2()

drive.info()
