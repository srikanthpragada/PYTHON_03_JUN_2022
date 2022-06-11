
largest = 0
while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break

    if num > largest:
        largest = num


print(largest)


