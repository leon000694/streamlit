print()
import requests
import parsel
"""
**程式功能: 先取網站文章所有章節url/再自url取文章內容/清洗資料/寫入.txt檔案
"""
url = 'http://www.h528.com/post/category/%e4%ba%ba%e5%a6%bb%e7%86%9f%e5%a5%b3/page/04'
headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

def get_book_links(url): #取得網頁中所有章節url
    response = requests.get(url)
    response.encoding = response.apparent_encoding #萬能解碼    
    html = response.text
    sel = parsel.Selector(html)
    links = sel.css('h3 a::attr(href)').extract() #清出所有章節links
    return links

def download_one_chapter(link):
    response = requests.get(link, headers=headers)
    response.encoding = response.apparent_encoding #萬能解碼
    html = response.text
    sel = parsel.Selector(html)  #把字符串變成對象
    title = sel.css('#content h2::text').extract_first() # extract提取第一個標籤的內容
    contents = sel.css('#content p::text').extract()  # 提取所有的內容
    """ 數據清除(清除空白字符串) """
    contents1 = [content.strip() for content in contents] #清二端空白
    # 把列表編成字符串
    text = '\n'.join(contents1)  # 將列表[]轉成字符串
    """ 保存小說內容 """
    file = open('Crawler/download/' + title +'.txt', mode='w', encoding='utf-8')
    file.write(title + '\n') # 是否將title存入新檔(只能寫入字符串)
    file.write('\n'+text)  # 是否將text 存入新檔(只能寫入字符串) 
    file.close()


if __name__ =='__main__':
    links = get_book_links(url)
    i = 1
    for link in links:
        if i <= 50: #最多執行次數(全部下載)
            print(i) 
            #download_one_chapter(link)      #==========1 (1 or 2 擇一)
            
            if i == 7: #單篇下載(擇一)
                download_one_chapter(link)  #==========2 (1 or 2 擇一)
                print() 
            i = i + 1
        else:
            break     

print()
# https://www.youtube.com/watch?v=bFpaYcdHjhU 
""" 爬蟲專用
print('<變前>',contents1) #============================
print('<變後>',text     ) #============================
"""