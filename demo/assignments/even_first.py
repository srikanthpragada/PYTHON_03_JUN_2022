
nums = []
while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break

    if num % 2 == 0:
        nums.insert(0,num)
    else:
        nums.append(num)

for n in nums:
    print(n)
