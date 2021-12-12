import requests
import time
import re

print()
class EastMoneySpider(self,page):
    def request(self,page):
        dt = int(round(time.time()*1000))
        print("dt= ",dt)
        url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=1,200&dt=1616888120957&atfc=&onlySale=0",format(page,dt)
        heads = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        }
        response = requests.get(url,headers=heads)
        self.convertStr2List(response.text)
    def convertStr2List(self,resText):
        pattern = re.compile(r"datas:(.*),count,showday")
        resStr = pattern.search(resText).group(1)
        

print()
# HTTP型態: https://www.ptt.cc/bbs/movie/index.html  https://www.motorim.org.tw/query/query_check.aspx 
# JSON型態: https://medium.com   https://cn.investing.com/equities/baidu.com  