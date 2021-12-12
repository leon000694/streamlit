print()
import cv2.cv2 as cv2
import os

root_F = 'D:/python-training/0_frequent/pic_resize/origin-picture/'

SH = SW = int(input('請輸入要縮放後照片的寬或高...(800px約219k):'))
for root, dirs, files in os.walk(root_F): # 路徑/根目錄/檔名
    for file in files:
        if os.path.splitext(file)[1] == '.jpg' or os.path.splitext(file)[1] == '.JPG':
            PathFile = root_F + file
            img = cv2.imread(PathFile, cv2.IMREAD_UNCHANGED)
            OH = int(img.shape[0]) #原圖高
            OW = int(img.shape[1]) #原圖寬
            O_HWRatio = OH/OW
            if O_HWRatio >= 1: #瘦高
                Ratio = SH/OH  #縮放比
            else:              #矮胖
                Ratio = SW/OW  #縮放比
            NH = int(OH * Ratio)
            NW = int(OW * Ratio)
            resized = cv2.resize(img, (NW, NH), fx=0, fy=0, interpolation=cv2.INTER_AREA)

            #cv2.putText(resized, 'Leon', (200, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA) #需否刻入名字

            file_O = f'D:/python-training/0_frequent/pic_resize/R-{file}'
            cv2.imwrite(file_O, resized) ##
            size = (os.path.getsize(file_O))/1000
            print(file,'縮放後圖檔大小約 = %d kbytes' %(size))
print()


# HTTP型態: https://www.ptt.cc/bbs/movie/index.html  https://www.motorim.org.tw/query/query_check.aspx 
# JSON型態: https://medium.com   https://cn.investing.com/equities/baidu.com  