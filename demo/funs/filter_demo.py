def iseven(n):
    return n % 2 == 0


l = [1, 2, 3, 4, 5]

for n in filter(iseven, l):
    print(n)

for c in filter(str.isupper, "AbcXyz"):
    print(c)
