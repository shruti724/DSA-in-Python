# class Student:
#     def __init__(self):
#         self.name = "Rohan"
#         self.rollNo = 23
#
#
# s = Student()
# # s.state = "Haryana"
# print(s.__dict__)
#

# class Student:
#
#     def __init__(self, name, rollNumber):
#         self.name = name
#         self.rollNumber = rollNumber
#
#
# s = Student("Priya", 14)
# print(s.__dict__)


# class Student:
#
#     def __init__(self, name, age):
#         self.name = "Rohan"
#         self.age = 20
#
#     def print_student_details(self):
#         print(self.name, end="")
#         print(self.age)
#
#
# s = Student()
# s.print_student_details()
# #
# AttributeError: 'Student' object has no attribute 'name'

# class Student:
#     def __init__(self, name, age):
#         self.name = "Rohan"
#         self.age = 20
#
#     def print_student_details():
#         print(self.name, end=" ")
#         print(self.age)
#
#
# s = Student("Parikh", 25)
# s.print_student_details()
#
# print_student_details() takes 0 positional arguments but 1 was given


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_student_details(self):
        print(self.name, end=' ')
        print(self.age)


s = Student("Rohan", 60)
s.print_student_details()

