print()
url = "https://www.ptt.cc/bbs/movie/index.html"
import requests
from bs4 import BeautifulSoup

r = requests.get(url) 
soup = BeautifulSoup(r.text,"html.parser")
# print(soup)
# print()

sel = soup.select("div.title a")
# print(sel)
# print()

for s in sel:
    print(s["href"], s.text)

print()
# https://www.ptt.cc/bbs/movie/index.html  