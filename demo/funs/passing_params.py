def zero(v):
    print(id(v))
    v = 0
    print(id(v))


def prepend(lst, value):
    lst.insert(0, value)


a = 100
print(id(a))
zero(a)
print(a)

l = [1, 2, 3]
prepend(l, 10)
print(l)
