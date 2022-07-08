FILENAME = "test.txt"

with open(FILENAME, "rt") as f:
    lines = []
    for line in f.readlines():
        if len(line.strip()) > 0:  # non-blank line
            lines.append(line)

with open(FILENAME, "wt") as f:
    for line in lines:
        f.write(line)
