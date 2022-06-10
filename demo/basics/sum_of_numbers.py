# take 10 numbers or until 0 is given whichever comes first

total = 0
for i in range(10):
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break
    if num < 0:
        continue

    total += num

print(total)
