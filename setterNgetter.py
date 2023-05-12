class Student():
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setFaculty(self, faculty):
        self.faculty = faculty
    def getFaculty(self):
        return self.faculty
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    
name = int(input("Enter the number of students:"))
for i in range(name):
    s = Student()
    s.setName(input("Enter the name:"))
    s.setFaculty(input("Enter the faculty:"))
    s.setAge(int(input("Enter the age:")))
    print("Name is:",s.getName(), "faculty is", s.getFaculty(),"age is:" ,s.getAge())





    