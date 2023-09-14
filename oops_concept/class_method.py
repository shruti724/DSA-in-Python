from datetime import date

class Student:

    def __init__(self, name, age=15, percentage=80):
        self.name = name
        self.age = age
        self.percentage = percentage

    @classmethod
    def fromBirthYear(cls, name, year, percentage):
        return cls(name, date.today().year - year, percentage)

    def studentDetails(self):
        print("Name= ", self.name)
        print("Age= ", self.age)
        print("Percentage= ", self.percentage)


s1 = Student("Anny")
s1 = s1.fromBirthYear("Pal", 1994, 60)
s1.studentDetails()


# output:
# Name=  Anny
# Age=  29
# Percentage=  60
