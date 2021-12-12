print()
"""
**功能: 
**使用方法方法: openpyxl.load_workbook()_['Sheet']_.cell_
**cell(row, column, value)  寫入資料，三個引數分別是行，列，值 
**cell(row, column).value  獲取指定單元格的值，兩個引數分別是行，列 
**workbook.remove('表單名')  刪除表單 ；del workbook['表單名']  刪除表單 
**sheet.max_row  獲取表單資料的總行數 ；sheet.rows  獲取按行所有的資料 
"""
import openpyxl

wb = openpyxl.load_workbook('1.xlsx') # 開啟工作簿
sh = wb['Sheet1'] # 獲取表單名
cell = sh.cell(row=1, column=1).value # 讀單元格的值
print("1. ",cell)
print()

cell = sh['A6'].value # 方式一：讀取A6單元格的值
print("2. cell= ",cell)
print()

cell = sh['A1':'B3'] # 讀取A1-B4的單元格，共8個單元格
print("cell= ",cell)
print("3")

cell = sh['A1:B3'] # 讀取A1-B4的單元格，共8個單元格
print("cell= ",cell)
print("4")

cell = sh[2] # 讀取第2行的單元格
print("cell= ",cell)
print("5")


cell6 = sh[1:2] # 讀取第1-2行的單元格
print("cell= ",cell)
print()
print("6")

sh = wb['Sheet1'] # 獲取表單
# 讀取指定的單元格資料
res1 = sh.cell(row=1, column=1).value
print("A1=",res1)
print("7")
# 獲取最大行數
print("最大行: ",sh.max_row)
# 獲取最大列數
print("最大列: ",sh.max_column)  # sheet.max_column  獲取表單資料的總列數 ；
print("8")
# 按列讀取所有資料，每一列的單元格放入一個元組中
# print(sh.columns)   # 直接列印，列印結果是一個可迭代物件，我們可以轉換成列表來檢視

# 按行讀取所有資料，每一行的單元格放入一個元組中
rows = sh.rows
# print(list(rows))   # 轉換成列表之後列印結果為具體的單元格，如下

# 我們可以通過for迴圈以及value來檢視單元格的值
for row in list(rows):  # 遍歷每行資料
    case = []   # 用於存放一行資料
    for c in row:  # 把每行的每個單元格的值取出來，存放到case裡
        case.append(c.value)
    print(case)

print()