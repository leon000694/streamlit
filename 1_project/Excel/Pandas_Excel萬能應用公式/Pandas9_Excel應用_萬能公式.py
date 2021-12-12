print()
import pandas as pd
import os

""" 讀excel ====================== """
dfs = []
print(os.getcwd()) #取得目前的目錄
print()

os.chdir("D:/python-training/1_project/Excel/Pandas_Excel萬能應用公式") #設定要切換的目錄
for root,dirs,files in os.walk('.'): #遍歷目錄下所有檔案
    for file in files:
        if file.endswith('.xlsx'): #========> 判別文件夾下所有.xlsx的檔案
            df = pd.read_excel(file)
            dfs.append(df) #迭代所有excel內容
print('A', dfs)
print()

for df in dfs:
    # 新增一列列名:年終獎金
    df['年終獎金'] = ''
    for index,row in df.iterrows():
        score = row['績效']
        group = row['項目組']
        #判別項目組值為項目組1時，修正為項目組5
        if group == '項目組1':
            row['項目組'] = '項目組5'
        #依不同分數給予不同年終獎金
        bonus = 0
        if score > 95:
            bonus = 8000
        elif score > 90:
            bonus = 6000
        else:
           bonus = 4000 
        row['年終獎金'] = bonus
        df.iloc[index] = row #必須重新賦值回去，重要!
print('B',dfs)
print()

#合併表格
new_df = pd.concat(dfs, ignore_index=True)
print('C',new_df)

#保存
new_df.to_excel("temp.xlsx",index = False)

print()
# 教學網址: https://www.youtube.com/watch?v=6kzFjn5-U40&t=268s 
# 使用方法: os[.getcwd()/.chdir("")/for root,dirs,files in os.walk('.')/.endswith]_pandas(.read_excel/.append/iloc[index])