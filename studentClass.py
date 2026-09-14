class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def student_profile(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    def is_pass(self):
        if self.marks >= 40:
            return "pass"
        else:
            return "fail"


student1 = Student("Arun", 21, 75)
student2 = Student("Rahul", 22, 35)

student1.student_profile()
print("result:",student1.is_pass())

print()

student2.student_profile()
print("Result:", student2.is_pass())