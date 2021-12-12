print()
#from openpyxl import Workbook, load_workbook
import pandas as pd
import os


## 建立參數df (dataframe)
print('**目前目錄為:\n', os.getcwd(), '\n') #取得目前的目錄
os.chdir("D:/python-training/1_project/M13-重要業務參數") #設定要切換的目錄
for root,dirs,files in os.walk('.'): #遍歷目錄下所有檔案
    for file in files:
        if file.endswith('.xlsx'): 
            df = pd.read_excel(file)
            #dfs.append(df) #迭代所有excel內容
print('**測試結果為:\n', df)
df.to_excel("temp.xlsx", index = False)


print('<程式執行完成...> '+'\n', )