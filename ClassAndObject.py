# Python Class and Object
class Parrot:
  #attribute
  name = ""
  age = 0
#crate a parrot object
parrot1 = Parrot()
parrot1.name = "Meu"
parrot1.age = 10


# create a another parrot object
parrot2 = Parrot()
parrot2.name = "Baa"
parrot2.age = 4

#access the attribute and print it
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")
