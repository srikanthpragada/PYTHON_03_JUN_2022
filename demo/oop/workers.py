from abc import ABC, abstractmethod

# Abstract class
class Worker(ABC):
    def __init__(self, name, work):
        self.name = name
        self.work = work

    def __str__(self):
        return f"{self.name} - {self.work}"

    @abstractmethod
    def getsalary(self):
        pass


class HourlyWorker(Worker):
    def __init__(self, name, work, hours, rate):
        super().__init__(name, work)
        self.hours = hours
        self.rate = rate

    @property
    def hourrate(self):
        return self.rate

    @property
    def hoursworked(self):
        return self.hours

    def __str__(self):
        return f"{super().__str__()} - {self.hours} - {self.rate}"

    def getsalary(self):
        return self.hours * self.rate


class WeeklyWorker(Worker):
    def __init__(self, name, work, weeks, rate):
        super().__init__(name, work)
        self.weeks = weeks
        self.rate = rate

    @property
    def weekrate(self):
        return self.rate

    @property
    def weeksworked(self):
        return self.weeks

    def __str__(self):
        return f"{super().__str__()} - {self.weeks} - {self.rate}"

    def getsalary(self):
        return self.weeks * self.rate


hp = HourlyWorker("David", "DBA", 10, 1000)
print(hp.getsalary())
print(hp.hoursworked)

wp = WeeklyWorker("Scott", "Programmer", 3, 10000)
print(wp.getsalary())
print(wp.weekrate)

