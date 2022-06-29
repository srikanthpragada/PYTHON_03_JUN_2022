class Counter:
    def __init__(self, start=1):
        self.value = start

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def getvalue(self):
        return self.value


c = Counter(10)
c.increment()
c.decrement()
c.decrement()
print(c.getvalue())
