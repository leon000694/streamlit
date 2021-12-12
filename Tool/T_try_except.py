print() 
import requests
from bs4 import BeautifulSoup

def main():
	url1 = 'http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'
	bad_url = 'http://non-existed.domain/connect.html'
	#text1 = get_tag_text(url1, 'h1')
	#print('1.',text1, '\n')

	#text2 = get_tag_text(url1, 'h2')
	#print('2.',text2,'\n')

	text3 = get_tag_text(bad_url, 'h1')
	print('3.',text3,'\n')

def get_tag_text(url, tag):
	try:
		resp = requests.get(url)
		if resp.status_code == 200:
			soup = BeautifulSoup(resp.text, 'html.parser')
			return soup.find(tag).text
	except Exception as e:
		print('Exception: %s' %e)
	return None

if __name__ =='__main__':
	main()


#print('運行結束... \n')