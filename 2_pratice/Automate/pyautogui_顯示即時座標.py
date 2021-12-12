print()
import pyautogui,time

try:
    while True:
        x,y = pyautogui.position()
        positionStr = 'X: '+str(x).rjust(4)+' Y:'+str(y).rjust(4)
        pix = pyautogui.screenshot().getpixel((x,y))   # 獲取滑鼠所在螢幕點的RGB顏色
        positionStr += ' RGB:('+str(pix[0]).rjust(3)+','+str(pix[1]).rjust(3)+','+str(pix[2]).rjust(3)+')'
        print(positionStr,end='')                      # end='' 替換了預設的換行
        print('\b'*len(positionStr),end='',flush=True) # 連續退格鍵並重新整理，刪除之前列印的座標，就像直接更新座標效果
except KeyboardInterrupt:                            # 處理 Ctrl-C 按鍵
    time.sleep(0.5)