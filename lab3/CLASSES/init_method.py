# __init__ constructor example

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Ali", 20)
print(student1.name, student1.age)
