class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def totalseconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def __eq__(self, other):
        return self.totalseconds() == other.totalseconds()

    def __gt__(self, other):
        return self.totalseconds() > other.totalseconds()

    def __int__(self):
        return self.totalseconds()

t1 = Time(10, 10, 10)
print(int(t1))   # t1.__int__()
# t2 = Time(10, 10, 10)
# print(t1)
# print(t1 == t2)  # t1.__eq__(t2)
# print(t1 > t2)

times = [Time(1, 2, 3), Time(1, 1, 1), Time(10, 20, 30), Time(5, 5, 5)]
for t in sorted(times):
    print(t)