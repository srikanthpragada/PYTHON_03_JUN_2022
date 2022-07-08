import os

entries = os.walk(r"d:\classroom\jun3\demo")
count = 0
for (dirname, dirs, files) in entries:
    for file in files:
        if file.endswith(".py"):
            count += 1
            print(dirname + "\\" + file)

print("Count = ", count)
