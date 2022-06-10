# Common factors
num1, num2 = 40, 21
small = min(num1, num2)

for i in range(2, small // 2 + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i, end=' ')

