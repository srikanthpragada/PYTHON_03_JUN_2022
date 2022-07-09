import re

st = """
  First line
  Second Line   
  Third     Line.  More     spaces...
         Fourth      Line
"""

for line in st.split("\n"):
    print(re.sub('\s+', ' ', line.strip()))
