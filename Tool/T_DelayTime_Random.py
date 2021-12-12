print()
url = "https://www.ptt.cc/bbs/movie/index.html" 
import random
import time
import requests
from bs4 import BeautifulSoup

r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
sel = soup.select("div.title a")
for s in sel:
    delay_choices = [1, 2]  # 延遲的秒數
    delay = random.choice(delay_choices) # 隨機選取秒數
    time.sleep(delay)       # 延遲的秒數
    print(s["href"], s.text)
print()

# https://www.ptt.cc/bbs/movie/index.html  