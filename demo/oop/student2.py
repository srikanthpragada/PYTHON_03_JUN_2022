class Student2:
    # static variable / class attribute
    courses = {'python': 10000, 'java': 8000, 'c': 5000}

    @staticmethod
    def getfee(course):
        return Student2.courses.get(course, None)

    def __init__(self, admno, name, course='python'):
        self.admno = admno
        self.name = name
        self.course = course.lower()
        self.feepaid = 0

    def payment(self, amount):
        self.feepaid += amount

    def __str__(self):
        return f"{self.admno} - {self.name} - {self.course} - {self.feepaid}"

    def totalfee(self):
        return Student2.courses[self.course]

    @property
    def dueamount(self):
        return self.totalfee() - self.feepaid


s1 = Student2(1, 'Mark', 'Java')
s1.payment(5000)
print(s1.getdue())

s2 = Student2(2, "Jack")
print(s2.dueamount)
