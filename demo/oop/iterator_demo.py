s = "Hello"

# for c in s:
#     print(c)

si = s.__iter__()
while True:
    try:
        v = si.__next__()
        print(v)
    except:
        break
