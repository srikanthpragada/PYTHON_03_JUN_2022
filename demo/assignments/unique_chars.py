names = ["java", "c#", "python", "javascript", "sql"]

chars = set()   # Empty set 
for n in names:
    chars = chars | set(n)

print(chars)


