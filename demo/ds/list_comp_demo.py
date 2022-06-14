# lst = []
# for n in range(1,11):
#     lst.append(n * n)

lst = [n * n for n in range(1, 11)]
print(lst)

codes = [ord(c) for c in "Python" if c.islower()]
print(codes)
