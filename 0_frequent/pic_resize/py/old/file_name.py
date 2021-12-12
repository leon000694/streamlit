# -*- coding: utf-8 -*-
print() 
import os

def file_name(file_dir='D:/python-training/0_frequent/pic_resize/origin-picture'):
	L=[]
	for root, dirs, files in os.walk(file_dir):
		for file in files:
			if os.path.splitext(file)[1] =='.jpg' or os.path.splitext(file)[1] =='.JPG':
				L.append(os.path.join(file))
	return L

#L = file_name()
#print(L)
#print('運行結束... \n')