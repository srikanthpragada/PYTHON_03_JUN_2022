st = 'how do you do'

processed = ""
for c in st:
    if c not in processed:
        print(c, st.count(c))
        processed += c

