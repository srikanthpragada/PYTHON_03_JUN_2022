# Take a number and display factors
num = int(input("Enter number :"))

for i in range(2, num//2 + 1):
    if num % i == 0:
        print(i, end=' ')
