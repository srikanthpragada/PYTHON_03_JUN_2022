def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


print(isprime(10), isprime(11))
for n in range(1, 50):
    if isprime(n):
        print(n)
