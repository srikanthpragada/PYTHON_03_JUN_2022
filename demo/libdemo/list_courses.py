from bs4 import BeautifulSoup

with open("courses.xml", "rt") as f:
    contents = f.read()

bs = BeautifulSoup(contents, 'lxml-xml')
courses = bs.find_all("course")
for course in courses:
    title = course.find("title").text
    duration = course.find("duration").text
    fee = course.find("fee").text
    currency = course.find("fee")['currency']
    print(f"{title:30} {int(duration):3}  {int(fee):5} {currency}")









