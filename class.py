class Person:
    def __init__(self, name, adddress,age):
        self.name = name
        self.adddress = adddress
        self.age = age
    def details(self):
        print("hello my name is " , self.name , ". I live in " , self.adddress , "and I am " , self.age, "years old")

person1 = Person("Roshan", "manamaiju", 20)
person1.details()

