print()
#儲存檔案
file = open('temp.txt', mode='w', encoding='utf-8')
file.write('測試中文 Hello File\nSecond Line') #操作
file.close()
