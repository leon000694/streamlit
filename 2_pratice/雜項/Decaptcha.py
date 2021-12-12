print()
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from sklearn.preprocessing import binarize
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import pyautogui

#input('去噪點,h=15 & hcolor=15')
Image.open('captcha.png')
img = cv2.imread('captcha.png')
dst = cv2.fastNlMeansDenoisingColored(img, None, 20,20,7,21)
plt.subplot(121)
plt.imshow(img)
plt.title('raw img')
plt.subplot(122)
plt.imshow(dst)
plt.title('denoisingColored')
plt.show() #對照圖
print(img.shape) #56H*149W

#input('黑白化-非黑即白')
ret,thresh = cv2.threshold(dst,127,255,cv2.THRESH_BINARY_INV) #colored black
plt.imshow(thresh)
plt.show() 
print(img.shape)

#input('平面化')
imgarr = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
plt.imshow(imgarr)
plt.title('convert to layer 1')
plt.show()
print(imgarr.shape)

# resize 56*149*1
imgarr = cv2.resize(imgarr,(149,56),interpolation=cv2.INTER_CUBIC) 

#input('sklearn線性回歸')
imgarr[:,5:144] = 0 #黑色碼為0
imagedata = np.where(imgarr == 255) #255代表白色
plt.scatter(imagedata[1], 56-imagedata[0], s=100, c='red', label='Cluster')
plt.show()

X = np.array([imagedata[1]])
Y = 56-imagedata[0]
poly_reg = PolynomialFeatures(degree=2)
X_ = poly_reg.fit_transform(X.T)
regr = LinearRegression()
regr.fit(X_, Y)
plt.scatter(X,Y, color='black')

X2 = np.array([[i for i in range(0,149)]])
X2_ = poly_reg.fit_transform(X2.T)
plt.scatter(X,Y, color='black')
plt.ylim(ymin=0)
plt.ylim(ymax=56)
plt.plot(X2.T, regr.predict(X2_), color='blue', linewidth =3)

newimg = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
c=3
for ele in np.column_stack([regr.predict(X2_).round(0),X2[0],]):
	pos = 56-int(ele[0])
	#if newimg[pos-4:pos+4,int(ele[1])] = 255:
	#newimg[pos-3:pos+3,int(ele[1])] = 0 #曲線交點處未改色
	newimg[pos-c:pos+c,int(ele[1])] = 255-newimg[pos-c:pos+c,int(ele[1])] #曲線交點處已改色

plt.subplot(121)
plt.imshow(thresh)
plt.subplot(122)
plt.imshow(newimg)
plt.show() #2對照圖

print()
# https://www.youtube.com/watch?v=4DHcOPSfC4c