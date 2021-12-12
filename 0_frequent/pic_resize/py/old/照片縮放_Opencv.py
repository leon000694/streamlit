print()
import numpy as np
import cv2.cv2 as cv2
import os

SH = SW = int(input('請輸入新照片需求寬或需求高_?px '))
#SH=600 # 設定(輸入)新圖框高 #<------------
#SW=800 # 設定(輸入)新圖框寬 #<------------
S_HWRatio = SH/SW

img = cv2.imread('D:/python-training/0_frequent/照片縮放/1.jpg', cv2.IMREAD_UNCHANGED) # 圖檔須放在D:\python-training\下
print('Original W, H:', img.shape) # 印出(高,寬,圖channel=3=rgb彩圖)
#img = np.rot90(img) # 讓圖片每次--逆時鐘旋轉90度(需要時再啟用)
#cv2.imwrite('1.jpg',img) # 有旋轉再存回原圖原路徑

OH =int(img.shape[0])
OW =int(img.shape[1]) # 原圖寬
O_HWRatio=OH/OW

if O_HWRatio >= S_HWRatio:
    Ratio = SH/OH # 以高之縮放比為基準(新較)
else:
    Ratio = SW/OW # 以寬之縮放比為基準

NW = int(OW * Ratio)
NH = int(OH * Ratio)

resized = cv2.resize(img, (NW, NH),fx=0,fy=0, interpolation=cv2.INTER_AREA)
print('Resized W, H:',resized.shape," 變比=",round(Ratio,1))

file_O = 'D:/python-training/0_frequent/照片縮放/9.jpg' #<------------
cv2.imshow("Temp Image", resized)
cv2.imwrite(fileO,resized)
cv2.waitKey(0)
cv2.destroyAllWindows() # 關閉所有OpenCV的視窗
size = (os.path.getsize(file_O))/1000
print('縮放後圖檔 = %d kbytes' %(size))

print()

# HTTP型態: https://www.ptt.cc/bbs/movie/index.html  https://www.motorim.org.tw/query/query_check.aspx 
# JSON型態: https://medium.com   https://cn.investing.com/equities/baidu.com  