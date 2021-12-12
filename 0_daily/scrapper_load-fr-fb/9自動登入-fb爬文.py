print()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import getpass
from constants import f_mail
import pyautogui, time

start = time.time()
x = 0.5
options = Options()
options.add_argument("--disable-notifications") #取消彈跳視窗

browser = webdriver.Chrome('D:/chromedriver', chrome_options=options)
browser.set_window_size(750,800)
browser.get("https://www.facebook.com/")
time.sleep(x)
email = browser.find_element_by_id("email") #定位
password = browser.find_element_by_id("pass") #定位
email.send_keys(f_mail)
time.sleep(6)

#輸入(隱藏)密碼
pyautogui.click(1560, 978)
f_pword = getpass.getpass('請輸入密碼:')
password.send_keys(f_pword)
time.sleep(x)
password.submit()
time.sleep(3)

browser.get('https://www.facebook.com/learncodewithmike')
time.sleep(x)
browser.set_window_size(750,800)
for x in range(1, 4):
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 'js'
	time.sleep(4)
soup = BeautifulSoup(browser.page_source, features='lxml') 
titles = soup.find_all('div', {'class': 'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'})
for title in titles:
	post = title.find('div', {'dir':'auto'})
	if post:
		print(post.getText())

browser.quit()
end = time.time()

print('\n','code ending...', end-start, '秒')
# https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html
