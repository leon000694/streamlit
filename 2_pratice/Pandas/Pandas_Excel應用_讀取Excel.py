print()
import pandas as pd

""" 一、Pandas **讀取Excel資料 ========================================== """
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx")
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx", sheet_name=None)
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx", sheet_name="2019")
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx", sheet_name=["2018", "2019"])

""" 二、Pandas 讀取Excel **欄資料 ======================================= """
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx",
#                     sheet_name="2019", usecols=["年別", "細分", "合計"])
# 指定欄位索引值
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx",
#                     sheet_name="2019", usecols=[3])
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx",
#                     sheet_name="2019", usecols=[0, 3, 17])
# 指定欄位名稱
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx",
#                     sheet_name="2019", usecols="A, D, R")
# 選取範圍欄位名稱
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx",
#                     sheet_name="2019", usecols="A, D, F:R")           

""" 三、Pandas 讀取Excel **列資料 ======================================= """
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx",
#                     sheet_name="2019", nrows=21) 

# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx")
# new_df = df[0:287] # 索引值 0-286(2012年)的列資料

""" 四、Pandas讀取Excel **儲存格資料 ==================================== """
# df = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx")
# d2 = df.at[0, "細分"] # 讀取D2儲存格的值(以"列"索引值及"欄位"標題來定位)
# d2 = df.iat[0, 3] # 讀取D2儲存格的值(以列索引值及欄索引值來定位)(右col3不含)
# print(d2)

""" 五、Pandas **合併Excel 活頁簿資料 =================================== """
# df = pd.DataFrame()
# data = pd.read_excel("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx", sheet_name=None)
# sheets = pd.ExcelFile("D:/python-training/.Tool/歷年國內觀光點遊客月統計.xlsx")
# for s_name in sheets.sheet_names:
#     df = pd.concat([df, data.get(s_name)], ignore_index=False) #串接資料

#print(df)
#print(new_df)
#df.to_excel('temp.xlsx')

print()
# https://www.learncodewithmike.com/2020/12/read-excel-file-using-pandas.html#more