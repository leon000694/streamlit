print()
def get_tag_text(url, tag):
	try:
		resp = requests.get(url)
		if resp.status_code == 200:
			soup = BeautifulSoup(resp.text, 'html.parser')
			return soup.find(tag).text
	except Exception as e:
		print('Exception: %s' %e)
	return None

print('運行結束... \n')