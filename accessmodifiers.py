#public
class Person:
    def __init__(self):
        self.name = "roshan"

per1 = Person()
print(per1.name)

#protected

class Emnployee:
    def __init__(self):
        self._name = "Roshan"

emp1 = Emnployee()
print(emp1._name)


#private
class Student:
    def __init__(self):
        self.__name = "Asmita"

stu = Student()
print(stu._Student__name) #Name mangling --> Private variable vanda agadi underscore ani Class name rakhyo vaney chai tyo private variable lai class vandaa bahira access garna milxa




