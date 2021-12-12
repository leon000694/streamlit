print()
import pandas as pd
path = 'D:/python-training/.Tool/'    #2私人電腦

""" 資料『型態』處理 """
#df = pd.read_csv(path + "mycsvfile.csv")
#df['title'] = df['title'].astype('string') # =======================> 將標題轉為字串
#print(df.dtypes) # =================================================> 印出資料型態

#df['id'] = pd.to_numeric(df['id'], errors='coerce') # =====> 資料轉為數字
df['date_added'] = pd.to_datetime(df['date_added']) # =========> 物件資料轉為日期
print(df(:))

""" 資料『格式』處理 """
# df['date_added'] = pd.to_datetime(df['date_added']).dt.strftime('%Y/%m/%d')
# df['rating'] = df['rating'].round(decimals = 0) # 四捨五入到整數位
# print(df)

""" 『自訂函式』清理資料 """
# 西元年轉民國年
# def convert_chinese_year(year):
#     return int(year)-1911

# df = pd.read_csv("mycsvfile.csv", converters={
#     'date_added': lambda x: pd.to_datetime(x),  # 新增日期轉為日期型態
#     'release_year': convert_chinese_year, # 轉為民國年
#     'rating': lambda x:int(round(float(x), 0)) # 評價欄位四捨五入
# })
#print(df)

# show_id欄位加上千分位符號
# df['show_id'] = df['show_id'].apply(lambda x:format(x,','))
# print(df)

print()