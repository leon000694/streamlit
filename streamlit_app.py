import time 
import streamlit as st
import numpy as np
import pandas as pd
from google.oauth2.service_account import Credentials
import gspread
import matplotlib.pyplot as plt

#(網頁配置設定)要寫在程式內所有 Streamlit命令之前
st.set_page_config(
	page_title='M13資訊交流網頁',
	page_icon='random',
	layout='wide', #centered
	initial_sidebar_state='expanded')

st.title('M13 資訊交流網頁')
st.write('111年度重要**參數表**: ')

## 讀取GS試算表(參數表)
scope = ['https://www.googleapis.com/auth/spreadsheets'] # Google API應用範圍
creds = Credentials.from_service_account_file("D:/python/Tool/T_gsheet_Credentials.json", scopes=scope) #金鑰
gs = gspread.authorize(creds) #驗證
gsheet = gs.open_by_url("https://docs.google.com/spreadsheets/d/1LJEUYcjOayfaKn1hiRbKRR3lPpj9unS1NvvPI2lcQZw/edit#gid=339883143") #M13重要業務參數表
worksheet = gsheet.get_worksheet(0)
df_F = pd.DataFrame(worksheet.get_all_records(head=1)) # 讀取google sheet Feed資料
df = df_F.iloc[0:12, lambda df_F:[0,1,2,3,4,5,6,7,8,9,10]] # .iloc[列, lambda df:[欄]]
df

fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(
	nrows=7, ncols=1, sharex=True, figsize=(7.5,5)) #(寬,高)
fig.tight_layout(pad=1)
ax1.plot(df['date'], df['電信費'],color='r')
ax2.plot(df['date'], df['網路費'],color='r')
ax3.plot(df['date'], df['fuel'],color='orange')
ax4.plot(df['date'], df['electricity'],color='c')
ax5.plot(df['date'], df['waterpower'],color='c')
ax6.plot(df['date'], df['KRTC-send'],color='limegreen')
ax6.plot(df['date'], df['KRTC-receive'],color='b')
ax7.plot(df['date'], df['TITC-send'],color='limegreen')
ax7.plot(df['date'], df['TITC-receive'],color='b')
ax1.set_ylabel('telecom', fontsize=8)
ax2.set_ylabel('network', fontsize=8)
ax3.set_ylabel('fuel', fontsize=8)
ax4.set_ylabel('electricity', fontsize=8)
ax5.set_ylabel('waterpower', fontsize=8)
ax6.set_ylabel('KRTC', fontsize=8)
ax7.set_ylabel('TITC', fontsize=8)
#plt.show()

#chart_data = pd.DataFrame(
#	np.random.randn(10, 3),
#	columns=['a', 'b', 'c'])
#st.line_chart(chart_data)

if st.checkbox('顯示地圖圖表'):
	map_data = pd.DataFrame(
		np.random.randn(5, 2) /[1000, 1000] + [22.585, 120.33],
		columns=['lat', 'lon'])
	st.map(map_data)

option = st.sidebar.selectbox(
	'你喜歡哪種動物?',
	['dog', 'cat', 'parrot', 'groundhog'])
'(喜歡的動物)你的答案: ', option

left_column, right_column = st.columns(2)
left_column.write ('==這是左邊欄位==')
right_column.write('==這是右邊欄位==')

expander = st.expander('點擊來展開...')
expander.write('如果你要顯示很多文字,但又不想佔大半空間,可以使用這種方式。')

#latest_iteration = st.empty()
#bar = st.progress(0)
#for i in range(50):
#	latest_iteration.text(f'目前進度 {2*i+2}%')
#	bar.progress(2*i+2)
#	time.sleep(0.1)

@st.cache(suppress_st_warning=True)
def expensive_computation(a):
	latest_iteration = st.empty()
	bar = st.progress(0)
	for i in range(50):
		latest_iteration.text(f'目前進度 {2*i+2}%')
		bar.progress(2*i+2)
		time.sleep(0.1)
	
	st.write(f'沒有快取: expensive_compution({a})')
	time.sleep(2)
	return a*2
a = st.slider('選擇一個數字', 0,5)
result = expensive_computation(a)
st.write('結果: ', result)


#st.markdown('
#This is app retrieves the list of the **S&P 500**'
#)
#st.sidebar.header('User Input Features')
#@st.cache
#def load_data():
#	url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
#	html = pd.read_html(url, header = 0)
#	df1 = html[0] 
#	return df1
#df1 = load_data()
#sector = df1.groupby('GICS Sector')
## Sidebar - selection
#sorted_sector_unique = sorted( df1['GICS Sector'].unique())
#selected_sector = st.sidebar.multiselect('Sector, sorted_sector_unique')
## Filtering data
#df1_selected_sector = df[(df1['GICS Sector'].isin(selected_sector))

##st.header('Display Companies in Selected Sector')
##st.write('Data Dimension: ' + str(df1_selected_sector.shape[0] +'?'))
#st.dataframe(df1_selected_sector)
## Plot Closing Price of Query Symbol
#def price_plot(symbol):
#	df1 = pd.DataFrame(data[symbol].Close)
#	df1['Date'] = df1.index
#	plt.fill_between(df1.Date, df1.Colse, color='skyblue', alpha=0.3)
#	plt.plot(df1.Date, df1.Close, color='skyblue', alpha=0.8)
#	plt.xticks(rotation=90)
#	plt.title(symbol, fontweight='bold')
#	plt.xlabel('Date', fontweight='bold')
#	plt.ylabel('Closing Price', fontweight='bold')
#	return st.pyplot()
#num_company = st.sidebar.slider('Number of Companies', 1,5)
##if st.button('Show Plots'):
#st.header('Stock Closing Price')
#for i in list(df1_selected_sector.Symbol)[:num_company]:
#	price_plot(i)




# https://blog.jiatool.com/posts/streamlit/
# https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
# https://github.com/leon000694/streamlit.git
