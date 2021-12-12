print()
"""
**程式功能: 開啟/執行VBA/
**使用方法: win32com.client.Dispatch_excel.Workbooks.Open()_.Application.Run("")
"""
import os
import win32com.client
import openpyxl

#開啟 Excel
excel = win32com.client.Dispatch("Excel.Application")

#開啟檔案
excel.Workbooks.Open(Filename="D:/python-training/1.xlsm")

#執行巨集程式
excel.Application.Run("1.xlsm!比對程式") #==============================> 主功能

#傳入參數 , 並取得計算結果
# result = excel.Application.Run("1.xlsm!比對程式")
# print(result)

#離開 Excel
excel.Application.Quit()

#清理com介面
del excel

print()