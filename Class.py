#How to create classes manually:
class house():
  def __init__(self, address, state, alarm, price):
    self.address = address
    self.state = state
    self.alarm = alarm
    self.price = price


house1 = house(1234, "california", False , 300000)
house2 = house(5678, "texas", True , 150000)

print(house1.state)
print(house2.price)

#Another example of a class variable is the name of the company that builds the houses:
class flat():
  compny_name = "Dhaka Builders"
  def __init__(self, address,state, alarm, price):
    self.address = address
    self.state = state
    self.alarm = alarm
    self.price = price
