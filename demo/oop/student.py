class Student:
    def __init__(self, admno, name, course='python'):
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = 0

    def payment(self, amount):
        self.feepaid += amount

    def __str__(self):
        return f"{self.admno} - {self.name} - {self.course} - {self.feepaid}"

    def totalfee(self):
        match self.course.lower():
            case 'python':
                fee = 10000
            case 'java':
                fee = 8000
            case _:
                fee = 5000
        return fee

    def getdue(self):
        return self.totalfee() - self.feepaid


s1 = Student(1, 'Mark', 'Java')
s1.payment(5000)
print(s1.getdue())

s2 = Student(2, "Jack")
print(s2.getdue())

