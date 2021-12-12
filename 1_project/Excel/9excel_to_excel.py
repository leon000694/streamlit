import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import datetime

today_ = datetime.date.today()

excel_file = xlrd.open_workbook("D:/python-training/Tool/krtc-contact.xlsx")
new_file = copy(excel_file)

filename = 'temp_'+str(today_)+'.xls'
new_file.save(filename)

print()