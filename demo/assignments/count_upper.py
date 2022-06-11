
st = "This is to Test"

count = 0
for c in st:
    code = ord(c)
    if code >= 65 and code <= 90:
        count += 1

print(count)
