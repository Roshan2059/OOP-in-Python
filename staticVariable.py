'''If the value of a variable is not varied from object to object, such type of variables we have to declare with in the class directly but outside of methods. Such type of variables are called Static variables.'''

class Student():
    faculty = "BCA"
    Semester = "6th" 
    #Here the faculty and semester are the static variables
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def display(self):
        print("Name : ", self.name)
        print("Faculty : ", self.faculty)
        print("Semester : ", self.Semester)
        print("Roll : ", self.roll)
        print("Marks : ", self.marks)

s1 = Student("Sudip", 1, 80)
s1.display()
s2 = Student("Asmita", 2, 70)
s2.display()
