num = 32323111
for i in range(2, num//2 + 1):
    if num % i == 0:
        print(f"Not prime because it has factors {i}")
        break
else:
   print("Prime number")

