import requests
import time
import re

print()
class EastMoneySpider:
    def request(self,page):
        #dt = int(round(time.time() * 1000))
        url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=1,200&dt=1616888120957&atfc=&onlySale=0".format(page)
        heads = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        }
        response = requests.get(url,headers = heads)
        self.convertStr2List(response.text)

    def convertStr2List(self,resText):
        pattern = re.compile(r"datas:(.*),count")
        resStr = pattern.search(resText).group(1)
        resStr = re.sub(r"\[",'',resStr)
        resStr = re.sub(r"\]",'',resStr)
        resStrList = resStr.split(',')
        result = []
        tmpList = []
        i = 0
        for resStr in resStrList:
            tmpList.append(resStr)
            i += 1
            if i % 21 == 0:
                result.append(tmpList)
                tmpList = []
                print(i)
        print("將字符串轉換為列表",result)

if __name__ == "__main__":
    moneySpider = EastMoneySpider()
    for page in range(2,4):
        print("Spider page{0}---".format(page))
        moneySpider.request(page)

print()
# HTTP型態: https://www.ptt.cc/bbs/movie/index.html  https://www.motorim.org.tw/query/query_check.aspx 
# JSON型態: https://medium.com   https://cn.investing.com/equities/baidu.com  
