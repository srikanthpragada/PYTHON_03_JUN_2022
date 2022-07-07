f = open("marks.txt", "rt")

for m in sorted(f.readlines(),
                key=lambda v: int(v),
                reverse=True):
    print(m.strip())



f.close()
