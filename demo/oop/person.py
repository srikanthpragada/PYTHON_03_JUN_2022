class Person:
    def __init__(self, name, mobile):
        self.name = name
        # private attribute
        self.__mobile = mobile


p1 = Person("Steve", "39399339")
print(p1.__dict__)
print(p1._Person__mobile)

