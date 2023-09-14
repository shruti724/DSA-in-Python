# class Apple:
#     def fruit(rat):
#         pass
#
#
# s = Apple()
# print(s.fruit())

# class Apple:
#     pass
#
#
# s = Apple()
# print(s)
# <__main__.Apple object at 0x0000020FA5FC8400>


# class Student:
#     pass
#
#
# s1 = Student()
# print(type(s1))
# l = list()
# print(type(l))
#
# <class '__main__.Student'>
# <class 'list'>

# class Student:
#     name = "Roy"
#     roll = 12
#
#
# s1 = Student()
# print(s1.name)

# class Student:
#     passingPercentage = 80
#     def studentDetails(self):
#         self.name = "Riya"
#         print("Name= ", self.name)
#         percentage = 40
#         print("Precentage= ", percentage)
#
#     def isPassed(self):
#         if percentage > Student.passingPercentage:
#             print("passed")
#         else:
#             print("Not passed")
#
# s1 = Student()
# s1.studentDetails()
# s1.isPassed()
#
# NameError: name 'percentage' is not defined


# class Student:
#     passingPercentage = 80
#     def studentDetails(self):
#         self.name = "Riya"
#         print("Name= ", self.name)
#         self.percentage = 40
#         print("Precentage= ", self.percentage)
#
#     def isPassed(self):
#         if self.percentage > Student.passingPercentage:
#             print("passed")
#         else:
#             print("Not passed")
#
# s1 = Student()
# s1.studentDetails()
# s1.isPassed()


# class Student:
#     name = "Atul"
#
#     def store_detail(self):
#         self.age = 60
#
#     def print_age(self):
#         print(self.age)
#
# s = Student()
# s.store_detail()
# s1 = Student()
# # s1.store_detail()
# s1.print_age()
#
# AttributeError: 'Student' object has no attribute 'age'




