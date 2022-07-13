html = """
<html>
<body>
<h1 style='color:red'>HTML </h1>
<p>This it to test Beautiful Soup. </p>
<p>For more details, please visit : <a href="https://www.crummy.com/software/BeautifulSoup">Official Website </a>
</body>
</html>
"""

from bs4 import BeautifulSoup

bs = BeautifulSoup(html, 'html.parser')
print(bs.h1)
print(bs.h1.text)
print(bs.h1.attrs)
print(bs.h1['style'])

for p in bs.find_all("p"):
    print(p.text)




