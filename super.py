# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# class Programmer(Employee):
#     def __init__(self, name, salary, languages_known):
#         super().__init__(name, salary)
#         self.languages_known = languages_known

# emp1 = Employee("Roshan", 50000)
# print(emp1.name)
# print(emp1.salary)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def showEmpDetail(self):
        print(f"Name : {self.name}, Salary : {self.salary}")

class Programmer(Employee):
    def __init__(self, name, salary, language_known):
        super().__init__(name, salary)
        self.language_known = language_known

    def progdetail(self):
        super().showEmpDetail()
        return f"Primary language: {self.language_known}"
    
# emp = Employee("Roshan", 50000)
# details = emp.showEmpDetail()
# print(details)

prog = Programmer("Roshan Panta", 100000, "Python")
details = prog.progdetail()
print(details)