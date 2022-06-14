names = ['Scott', 'Mark', 'Bob']
ages = [30, 40, 34, 45]

for t in zip(names, ages, strict=True):
    print(t)
