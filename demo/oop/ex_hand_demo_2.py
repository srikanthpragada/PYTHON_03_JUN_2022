a = "10"
b = "a"

try:
    c = int(a) / int(b)
    print(c)
except ZeroDivisionError:
    print("Zero division error")
finally:
    print("Finally!")

print("The End")
