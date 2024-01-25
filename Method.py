#Methon in python OOP
class house():
  companyName = 'Dhaka Builders'
  priceUp = 1.08
  

  def __init__(self, address, state, alarm, price):
    self.address = address
    self.state = state
    self.alarm = alarm
    self.price = price
  
  def correctPrice(self):
    self.price *= self.priceUp

apartment1 = house(1234, "california", False , 300000)

apartment1.correctPrice()

print(apartment1.price)
