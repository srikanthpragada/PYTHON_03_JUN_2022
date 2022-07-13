from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

for a in bs.find_all("a"):
    href = a['href']
    if href.startswith("javascript:void"):
        continue

    if not href.startswith("http"):
        if not href.startswith("/"):
            href = "/" + href
        href = WEBSITE + href

    print(href)


