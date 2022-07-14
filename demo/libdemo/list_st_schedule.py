from bs4 import BeautifulSoup
import requests
from datetime import *

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

cur_date = datetime.today()
course_table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = course_table.find_all("tr")

for row in rows[1:]:
    cols = row.find_all("td")
    title = cols[0].text
    sd_str = cols[2].text + "-" + str(cur_date.year)
    sd = datetime.strptime(sd_str, "%d-%b-%Y")  # str to date
    days = (sd - cur_date).days    # days from timedelta
    print(f"{title:50} {days} days to go...")

