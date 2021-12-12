import requests

## 設定HTTP Headers、HTTP Request timeout
headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
response = requests.get(url, headers=headers, timeout=5)

## 檢查HTTP Status Code
if response.status_code == 200: #正確
	#接續執行
#if response.status_code != 200: #不正確 return False

## 檢查爬取的元素是否存在
soup = BeautifulSoup(response.content, 'lxml')
title = soup.find('h3', {'class': 'post_title'})
if title:
	#接續執行
else:
	#顯示警告訊息或發送訊息給管理人員

## 例外處理機制
try:
	headers = {
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
	}
	response = requests.get(url, headers=headers, timeout=5)
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'lxml')
		titles = soup.find_all('h3', {'class':'post_title'})
		result = []
		for title in titles:
			if title:
				result.append(title.getText())
			else:
				print('元素不存在')
	else:
		print('回應結果錯誤')

except requests.ConnectionError as conn_ex:
	print('連線錯誤')
	print(str(conn_ex))
except requests.Timeout as timeout_ex:
	print('請求超過錯誤')
	print(str(timeout_ex))
except requests.RequestException as request_ex:
	print('請求發生錯誤')
	print(str(request_ex))
except Exeception as e:
	print('發生其他錯誤')
	print(str(e))


## 檔案輸入/出(I/O)機制；打包成List、Tuple、Dictionary
try:
	headers = {
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
	}
	response = requests.get(url, headers=headers, timeout=5)
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'lxml')
		titles = soup.find_all('h3', {'class':'post_title'})
		
		result = [] ###
		for title in titles:
			if title:
				result.append(title.getText())
			else:
				print('元素不存在')
	else:
		print('回應結果錯誤')

except requests.ConnectionError as conn_ex:
	print('連線錯誤')
	print(str(conn_ex))
except requests.Timeout as timeout_ex:
	print('請求超過錯誤')
	print(str(timeout_ex))
except requests.RequestException as request_ex:
	print('請求發生錯誤')
	print(str(request_ex))
except Exeception as e:
	print('發生其他錯誤')
	print(str(e))

finally:
	try:
		with open('post.txt', 'w') as file:
			file.write('\n'.join(result))
	except Exception as ex:
		print(str(ex))
