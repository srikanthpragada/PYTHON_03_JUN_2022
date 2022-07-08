import os

FILENAME = "test.txt"
TEMPFILE = "temp.txt"

with open(FILENAME, "rt") as sf:
    tf = open(TEMPFILE, "wt")
    for line in sf.readlines():
        if len(line.strip()) > 0:  # non-blank line
            tf.write(line)

tf.close()

# delete source file
os.remove(FILENAME)

# Rename temp as source
os.rename(TEMPFILE, FILENAME)



