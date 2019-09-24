# Doesn't work. Moving on to next

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
for i in soup.find_all("h2"):
    print(i.text)