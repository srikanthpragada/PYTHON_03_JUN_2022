data = ["1,50", "2,80", "1,90", "3,45", "2,90", "3,85"]

students = {}
for entry in data:
    parts = entry.split(",")
    rno = int(parts[0])
    marks = int(parts[1])

    if rno in students:
        students[rno] = students[rno] + marks
    else:
        students[rno] = marks

    # total = students.get(rno, 0) + marks
    # students[rno] = total

for rno, total in sorted(students.items()):
    print(f"{rno:4} {total:4}")
