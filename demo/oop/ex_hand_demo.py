a = "10"
b = "a"

try:
    c = int(a) / int(b)
    print(c)
except ZeroDivisionError:
    print("Zero division error")
except ValueError as ex :
    print("Sorry! Invalid Number! Error -->", ex)

print("The End")
