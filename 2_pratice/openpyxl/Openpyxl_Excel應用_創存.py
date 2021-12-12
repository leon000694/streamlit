print()
"""
**功能: 創立一個工作簿/表單_寫入儲存格值_Excel存檔
**使用方法方法: openpyxl(.Workbook/.creat_sheet/.cell/.save)
"""
import openpyxl

wb = openpyxl.Workbook() # 建立一個工作簿
sh = wb.create_sheet('表單1')
sh.cell(row=1, column=1, value="Python") # 寫入一個數據
wb.save('Sample.xlsx') # 儲存