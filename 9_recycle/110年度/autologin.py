print()
import pyautogui,time
import webbrowser

webbrowser.open("http://erp.krtc.com.tw/erp/login")
# try:
#     while True:
#         x,y = pyautogui.position()
#         positionStr = 'X: '+str(x).rjust(4)+' Y:'+str(y).rjust(4)
#         pix = pyautogui.screenshot().getpixel((x,y))   # 獲取滑鼠所在螢幕點的RGB顏色
#         positionStr += ' RGB:('+str(pix[0]).rjust(3)+','+str(pix[1]).rjust(3)+','+str(pix[2]).rjust(3)+')'
#         print(positionStr,end='')                      # end='' 替換了預設的換行
#         print('\b'*len(positionStr),end='',flush=True) # 連續退格鍵並重新整理，刪除之前列印的座標，就像直接更新座標效果
# except KeyboardInterrupt:                            # 處理 Ctrl-C 按鍵
#     pyautogui.PAUSE = 0.5
#     print()

# set these to the correct coordinates for your computer.
id_Field = (207,693)
keep_Field = (1400,1062)
loginButton = (722,693)
loginButtonColor = (236,236,236)
#loginAnotherLink = (725,738)
formData = [{'name':'000694','fear':'eavppers','source':'wand','robocop':4,'comments':'Tell us'}] #,
        #     {'name':'Bog','fear':'eaves','source':'crystal','robocop':4,'comments':'Big room'},
        #     {'name':'Kad','fear':'apple','source':'woold','robocop':1,'comments':'Nice day'},
        #     {'name':'Cace','fear':'ppers','source':'ball','robocop':5,'comments':'n/a'}
        #    ]

for person in formData:
    #print('>>> 3 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(3)
    while not pyautogui.pixelMatchesColor(loginButton[0],loginButton[1],loginButtonColor):
        time.sleep(3)
    pyautogui.click(id_Field[0],id_Field[1])       # 單擊第一個文字欄位輸入位置
    pyautogui.typewrite(person['name']+'\t')       # 輸入該域，並按下 tab 鍵，將焦點轉向下一個輸入框
    time.sleep(6) # 6秒內輸入password

    # pyautogui.typewrite(person['fear']+'\t')
    # if person['source'] == 'wand':
    #     pyautogui.typewrite(['down','\t'])
    # elif person['source'] == 'crystal':
    #     pyautogui.typewrite(['down','down','\t'])
    # elif person['source'] == 'woold':
    #     pyautogui.typewrite(['down','down','down','\t'])
    # elif person['source'] == 'ball':
    #     pyautogui.typewrite(['down','down','down','down','\t'])                
    # if person['robocop'] == 1:
    #     pyautogui.typewrite([' ','\t'])
    # elif person['robocop'] == 2:
    #     pyautogui.typewrite(['right','\t'])
    # elif person['robocop'] == 3:
    #     pyautogui.typewrite(['right','right','\t'])
    # elif person['robocop'] == 4:
    #     pyautogui.typewrite(['right','right','right','\t'])
    # elif person['robocop'] == 5:
    #     pyautogui.typewrite(['right','right','right','right','\t'])
    #pyautogui.typewrite(person['comments']+'\t')
    pyautogui.press('enter')
    time.sleep(1)

    # Click the Login
    #pyautogui.click(loginAnotherLink[0],loginAnotherLink[1])

for i in range(100):
    for j in range(10):
        time.sleep(60)
        k = i*10 + j
        print(k,'minutes',end='')
        print('\b'*(len(k)+7),end='',flush=True)
    pyautogui.click(keep_Field[0],keep_Field[1])


print()