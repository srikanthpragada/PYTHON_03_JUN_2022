class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"

    def setemail(self, email):
        self.email  = email


class Employee(Person):
    def __init__(self, name, email, job, company):
        super().__init__(name, email)
        self.job = job
        self.company = company

    def __str__(self):
        return super().__str__() + f"- {self.job} - {self.company}"

    def setjob(self, job):
        self.job = job


e = Employee("Larry","larry@gmail.com","Programmer","google")
e.setemail("larrypage@google.com")
print(e) # e.__str__()




