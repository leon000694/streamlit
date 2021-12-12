print()
# 教學網站 https://www.youtube.com/watch?v=bFpaYcdHjhU 

import requests
import parsel

""" 獲取網頁源代碼 """
heads = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

def get_book_links():
    book_url = 'http://www.shuquge.com/txt/8659/index.html' # ==================> 下載別的小說 直接換url即可
    response = requests.get(book_url)
    response.encoding = response.apparent_encoding
    html = response.text
    sel = parsel.Selector(html)
    links = sel.css('dd a::attr(href)').extract() # 取得所有章節網址 url
    return links

def download_one_chapter(target_url):
    response = requests.get(target_url, headers=heads)
    response.encoding = response.apparent_encoding #解碼 萬能解碼
    html = response.text
    """ 從網頁源代碼裡拿到信息 """
    sel = parsel.Selector(html)  # 把字符串變成對象

    # 偽類選擇器(選擇屬性).css選擇器(選擇標籤)
    # extract為scrapy方法，可直用
    title = sel.css('.content h1::text').extract_first()  # extract 提取第一個標籤的內容
    contents = sel.css('#content::text').extract()  # 提取所有的內容
    #print(contents)

    """ 數據清除(清除空白字符串) """
    contents1 = [content.strip() for content in contents]   # contents1 = [];   # for content in contents:
    #print(contents1)
    # 把列表編成字符串
    text = '\n'.join(contents1)  # 去除兩端空白字符
    print(title)
    print(text)

    """ 保存小說內容 """
    # open 操作文件 (寫入 讀取)
    # file = open(title+'.txt', mode='w', encoding='utf-8')
    # # 只能寫入字符串
    # file.write(title)
    # file.write(text)
    # file.close()
    
   
if __name__=='__main__':
    links = get_book_links() # ========================================================> 呼叫函式 get_book_links()
    i = 1
    for link in links:
        if i <= 1: # ==================================================================> 設定要執行(印出)的章數i
            download_one_chapter('http://www.shuquge.com/txt/8659/'+link) # ===========> 呼叫函式 download_one_chapter()
            i = i + 1
        else:
            break     

    print("")
