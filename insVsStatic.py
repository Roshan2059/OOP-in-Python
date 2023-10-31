class Student():
    faculty = "BCA"  # yaslai chai class variable pani vando raixa
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def details(self):
        print("name", self.name)
        print("faculty", self.faculty)
        print("age", self.age)
        print("gender", self.gender)

stu1 = Student("Roshan", 20, "male")
stu1.details()
stu2 = Student("Asmita", 21, "female")
stu2.details()
stu1.name = "sudip"
Student.faculty = "BIM"
stu1.details()
stu2.details()

