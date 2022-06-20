data = ['10,Jack', '20,Bob', '10,Jason', '20,Scott', '30,Herbert', '30,Tom', '20,Marshall']
depts = {}

for entry in data:
    deptno, name = entry.split(",")
    emps = depts.get(deptno, [])
    emps.append(name)
    depts[deptno] = emps

for deptno, emps in depts.items():
    print(f'{deptno} {",".join(emps)}')
