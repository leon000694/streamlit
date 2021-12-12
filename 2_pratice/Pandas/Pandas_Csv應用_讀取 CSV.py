print()
# 閱讀網址 https://ithelp.ithome.com.tw/articles/10232077

import pandas as pd

""" Series欄位(一維) ================================ """
# s1 = pd.Series([1, 4, 7, 10, 13, 16]) # 手工建立 Series
# print(s1)
# print()

# L1 = list(range(1,20,3))
# s1 = pd.Series(L1)
# print(s1)
# print()

# s2 = pd.Series(L1, index=[chr(ord('a')+i) for i in range(7)])
# print(s2)
# print()

# s3 = pd.Series({'小狗':50, '小貓':60, '小熊':25})
# print(s3)
# print()

""" DataFrame 表格(二維) =========================== """
# # 創建 DataFrame兩種方法(dict+list)
# scores = [{"姓名":"小華", "數學":90, "國文":80},
#           {"姓名":"小明", "數學":70, "國文":55},
#           {"姓名":"小李", "數學":45, "國文":75}]
# score_df = pd.DataFrame(scores)
# print(score_df)
# print()

# scores = {"姓名":["小華","小明","小李"],
#           "國文":[80,55,75],
#           "數學":[90,70,45]}
# score_df = pd.DataFrame.from_dict(scores)
# print(score_df)
# print()

# 讀取 csv 資料
scores = pd.read_csv('D:/python-training/.Tool/mycsvfile.csv', index_col = 0)
# 截取部分資料 loc, iloc
# print(scores.loc[:,'rating']) #===>loc:前[row]後[column]
# print()
# print(scores.loc[scores.type =='Movie','director'])
# print()
# print(scores.loc[:, 'type':'director']) #前row區只能用":""

# print(scores.iloc[:,:]) # ============>iloc:前[row]後[column]
# print()
# print(scores.iloc[0:2, :]) #row0含 row2不含;同range(0:2)
# print()
# print(scores.iloc[[0,3,6],7:9]) #col7含 col9不含;用法同range()
# print(scores.iloc[0:3,[5,7,9]]) #row0含 row3不含
# print()
# print(scores.iloc[[6], 0:4])
# print()

# print(scores.head(5))  # head方法(row1-5)
# print()
# print(scores[['title', 'rating']]) # 指定Columns
# print()

# (創建DF第一種方法) 取得 column的資料
# print(scores['rating'])
# print(scores[['type','cast','rating']])

# (創建DF第二種方法) 用python的切片語法
# print(scores[0:2]) # (不含row0 含row2)
# print(scores[scores.rating=='4.1'])
# ??? print(scores[scores['rating']>5.0]) # 條件篩選
# print(scores.T)

temp = scores[scores.rating >='9.0']
#print(temp)
#temp.to_excel('temp.xlsx')

print()