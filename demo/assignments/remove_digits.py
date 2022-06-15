st = "abc123- xyz,45d"

# lst = []
# for c in st:
#     if not c.isdigit():
#         lst.append(c)

lst = [c for c in st if not c.isdigit()]
print("".join(lst))
