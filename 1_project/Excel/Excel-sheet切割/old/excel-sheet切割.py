import pandas as pd
import openpyxl 

path = 'D:/P_冬服/'

#1 將調查後之「需求數量、型號變更、計算後鼓勵金」 置入產出之excel需求總表活頁簿
df_P = []
df_P = pd.read_excel(path+'1原始名單_P.xlsx',sheet_name=0, header=0,dtype={10:str}) 
""" header=0代表Row(0-indexed)-須設定dtype第10欄型號變更欄為字串否則會報錯 """
df_F = pd.read_excel(path+'2需求調查_F.xlsx',header=0) #F代表 Feed(餵資料者)
df_P["鼓 勵 金"] = '' #新增 鼓勵金欄
df_P["款別有誤"] = '' #新增 款別有誤欄

#賦值 每人各品項需求數量/型號變更值
for index,row in df_F.iterrows():	
	id_F    = row['職工編號']
	data0_F = row['您的款別']     #取F表各款別值以利與P表比對/以利找出 款別有出入者
	data1_F = df_F.iat[index,7]  #長襯數量
	data2_F = df_F.iat[index,8]  #長排汗衫
	data3_F = df_F.iat[index,9]  #外套數量
	data4_F = df_F.iat[index,10] #背心數量
	data5_F = df_F.iat[index,11] #型號變更

	a,b,c,d = 0,0,0,0 #鼓勵金額度先歸零
	if data1_F==0: #值0代表同仁選擇不領/可獲得鼓勵金
	   a=100 #鼓勵金
	if data2_F==0:
	   b=100 #鼓勵金
	if data3_F==0:
	   c=200 #鼓勵金
	if data4_F==0:
	   d=200 #鼓勵金

	for index,row in df_P.iterrows(): 
		id_P = row['職工編號']
		data0_P = row['款別']   #取P表各款別值以利與F表比對/以利找出 款別有出入者
		if id_P == id_F:  #判別 id是否相符
			df_P.iat[index,6] = data1_F
			df_P.iat[index,7] = data2_F
			df_P.iat[index,8] = data3_F
			df_P.iat[index,9] = data4_F
			df_P.iat[index,10] = data5_F
			df_P.iat[index,11] = a+b+c+d #個人鼓勵金總額
			if data0_P != data0_F:
				df_P.iat[index,12]='款別有誤'
			break		
# 資料回存成 Excel檔
df_P.to_excel(path+"需求總表_O1.xlsx", index = False, sheet_name='需求總表')

#2 將需求總表依款別複製並自動切分為各品項活頁簿
filename1 = path+'需求總表_O1.xlsx' #===>原始檔案
filename2 = path+'需求總表_O2.xlsx' #===>複製切分後檔案

# 將 filename1需求總表資料 轉給writer.book
wb = openpyxl.load_workbook(filename1)
writer = pd.ExcelWriter(filename2, engine='openpyxl')
writer.book = wb

# 將 需求總表 依款別欄內各款別/各品項 clone成各活頁簿
df = pd.DataFrame(pd.read_excel(filename1,sheet_name ='需求總表',dtype = object))
df['款別'] = df['款別'].fillna('NA') #缺失值以'NA'填充

for groupname, groupdf in df.groupby('款別'): 
	groupdf.sort_values(by=['性別','單位代碼'],inplace=True,na_position='first') #排序
	groupdf.to_excel(writer,sheet_name=groupname,index=False) #切成3款別活頁簿回存Excel
	for i in range(4): #輸入4為本次發放品項數
		groupdf1 = groupdf.iloc[:, [0,1,2,3,4,5,i+6,10,11]]
		item = groupdf.columns.values[i+6] #取得欄標題名(如長襯)
		groupdf1.to_excel(writer,sheet_name = groupname+'-'+str(item),index=False)

writer.save()
wb.close()