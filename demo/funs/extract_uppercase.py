
def extract_upper(s):
    uc = [c for c in s if c.isupper()]
    return "".join(uc)


values = ['AbcxyA','UeFF','ADEcdd']
# upper_values = [extract_upper(s) for s in values]
# print(upper_values)

for v in map(extract_upper, values):
    print(v)

