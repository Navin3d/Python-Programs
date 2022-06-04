name = input("Enter a Name : ")
if(isinstance(name, str)):
    print("The given name ",name ,"is string")
else:
    print("The name is of other type.")

class Person:
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def isAdult(self):
        if(self.age>18):
            print("He is Adult")

student1 = Person("Jay", 19)

print("The Name of student1 is : ", student1.name)
print("The Age of student1 is : ", student1.age)
student1.isAdult()

print("The student1 isinstance of Person : ", isinstance(student1, Person))
