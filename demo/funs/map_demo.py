def next_even(n):
    return n + 2 if n % 2 == 0 else n + 1

l = [10, 20, 33, 11, 56]

for v in map(next_even, l):
    print(v)

for c in map(ord, 'Hello'):
    print(c)
