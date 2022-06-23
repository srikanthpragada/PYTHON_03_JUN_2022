def first2(s):
    return s[:2]


l = ["Abc", "Pqr", "Def"]

for v in map(lambda v: v[:2], l):
    print(v)

for v in map(first2, l):
    print(v)
