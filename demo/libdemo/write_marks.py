# Write marks into marks.txt

f = open("marks.txt", "wt")
while True:
    marks = int(input("Enter marks [0 to stop] :"))
    if marks == 0:
        break

    f.write(f"{marks}\n")

f.close()



