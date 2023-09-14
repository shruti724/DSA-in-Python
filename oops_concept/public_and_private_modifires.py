class Student:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def studentDetails(self):
        print(self.__name)
        print(self.age)


s = Student("Pal", 23)
print(s.__dict__)
print(s.age)
s.age = 27
print(s.age)
s.name = "Any"
print(s.name)
s.studentDetails()

# output
# {'_Student__name': 'Pal', 'age': 23}
# 23
# 27
# Any
# Pal
# 27
# print(s.__name)
# AttributeError: 'Student' object has no attribute '__name' (as name is now a private variable)

# Name Mangling
# print(s._Student__name)
# Pal
