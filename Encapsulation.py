#create a class
class Computer:
  def __init__(self):
    self.__maxPrice = 400

  def sell(self):
    print("Selling price: {}".format(self.__maxPrice))

  def setMaxPrice(self, price):
    self.__maxPrice = price

#create a object
c = Computer()
c.sell()

#change the price
c.__MaxPrice = 500
c.sell()

#using parameter
c.setMaxPrice(500)
c.sell()
