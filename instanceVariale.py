'''If the value of a variable is varied from object to object, then such type of variables are called instance variables.
For every object a separate copy of instance variables will be created.'''
class Person:
    def __init__(self, name, adddress,age):
        self.name = name
        self.adddress = adddress
        self.age = age
    def details(self):
        print("hello my name is " , self.name , ". I live in " , self.adddress , "and I am " , self.age, "years old")
    def delAdddress(self):
        del self.adddress

person1 = Person("Roshan", "manamaiju", 20)
person1.details()
print(person1.__dict__)
del person1.name
print(person1.__dict__)
person1.delAdddress()
print(person1.__dict__)
person2 = Person("Rashmi", "manamaiju", 18)
person2.details()
person2.delAdddress()
print(person2.__dict__)