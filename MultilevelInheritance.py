#Multilevel Inheritence in python
class Super:
  def superMethod(self):
    print("this is a method of super class")

class Drived(Super):
  def drivedMethod(self):
    print("this is a method of drived class")

class Drived2(Drived):
  def drivedMethod2(self):
    print("this is a method of super class 2")

drive = Drived2()

drive.superMethod()
