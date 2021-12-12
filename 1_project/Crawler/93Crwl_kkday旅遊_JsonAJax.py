print()
import requests
 
class Kkday:
    def __init__(self, city_name):
        self.city_name = city_name  # 城市名稱屬性.

    def scrape(self):
        result = []  # 回傳結果
        if self.city_name:  # 如果城市名稱非空值 (True)
            url = f"https://www.kkday.com/zh-tw/product/ajax_productlist/?keyword={self.city_name}&cat=TAG_4_4&sort=rdesc"
            response = requests.get(url)    # 取得傳入城市的所有一日遊票券
            activities = response.json()["data"] # Json格式
            i = 1
            for activity in activities:
                title = activity["name"]    # 票券名稱
                link = activity["url"]      # 票券詳細內容連結
                price = activity["price"]   # 票券價格
                booking_date = activity["earliest_sale_date"]  # 最早可使用日期
                star = activity["rating_star"]  # 評價

                if i <= 20: # =====================================================> 設定最大執行(印出)的章數i
                    print(i," ",star," ",title,",",price,"元") # =================> 是否印出每一行程/星級/價位
                    # if i == 6:
                    #     result.append(dict(title=title, link=link, price=price, booking_date=booking_date, star=star, source="KKday"))
                    #     print(activity)
                    #     print(result) # =========================================> 是否印出詳細旅遊行程
                    #     print()
                    i = i + 1
                else:
                    break
                
        print()
        return result

		
demo = Kkday("高雄") # ==========================================================> 輸入想旅遊地點
demo.scrape()

print() 
# HTTP型態: https://www.ptt.cc/bbs/movie/index.html  https://www.motorim.org.tw/query/query_check.aspx  
# JSON型態: https://medium.com  https://www.kkday.com/zh-tw