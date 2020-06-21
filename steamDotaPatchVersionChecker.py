import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.dota2.com/patches/'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header).text

soup = BeautifulSoup(r, 'lxml')

# for tag in soup.find_all("p"):
#     if tag.text != 'Gameplay Update' :
#         pass
#         print("{0}: {1}".format(tag.name, tag.text))


temp = soup.find_all("p",  {"class": "PatchTitle"})


LatestpatchVersion = temp[0].contents[0]
print(LatestpatchVersion)
print(type(LatestpatchVersion))
