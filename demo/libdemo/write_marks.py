# Write marks into marks.txt

with open("marks.txt", "wt") as f:
    while True:
        marks = int(input("Enter marks [0 to stop] :"))
        if marks == 0:
            break

        f.write(f"{marks}\n")





