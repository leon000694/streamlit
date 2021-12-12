import pandas as pd
import openpyxl 

path = 'D:/python-training/1_project/Excel-sheet切割/'
filename1 = path+'各單位名單.xlsx' #===>原始檔案
filename2 = path+'各單位清單_O.xlsx' #===>複製切分後檔案

## 將 filename1需求總表資料 轉給writer.book
writer = pd.ExcelWriter(filename2, engine='openpyxl')
#wb = openpyxl.load_workbook(filename1)
#writer.book = wb
#wb.close()

## 將 需求總表 依款別欄內各款別/各品項 clone成各活頁簿
df = []
df = pd.DataFrame(pd.read_excel(filename1,sheet_name =0, header=1))
for groupname, groupdf in df.groupby('一級單位'): 
	groupdf.to_excel(writer,sheet_name=groupname,index=False) #切成單位別活頁簿回存Excel
writer.save()

print()