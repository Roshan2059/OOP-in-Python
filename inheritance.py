class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def show_details(self):
        print("Name : ", self.name)
        print("ID   : ", self.id)

class Manager(Employee):
    def __init__(self, department):
        self.department = department

    # @property
    # def get_department(self):
    #     return self.department
    # @get_department.setter
    # def set_department(self, value):
    #     self.value = value


    def get_department(self):
        print(f"The department this managaer is managing is {self.department} department")

emp1 = Employee("Roshan Panta", 10)
emp2 = Employee("Sourav Kumar", 56)
emp1.show_details()
print("\n")
emp2.show_details()

emp3 = Manager("IT")
emp3.get_department()

