st = "How are you today. How were you yesterday"
words = st.split(' ')

for w in sorted(set(words)):
    print(f"{w} - {words.count(w)}")
