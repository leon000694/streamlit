print()
import hashlib
import json

def register():
	name= input('請輸入您的帳號 ')
	pwd = input('請輸入您的密碼 ')

	m = hashlib.md5()             # <=====
	m.update(pwd.encode('utf-8')) # <=====
	res = m.hexdigest()           # <=====
	dict = {name: res}
	with open('密碼.json', 'a', encoding='utf-8') as f:
		json.dump(dict, f)
	print('\033[0;32m註冊成功!\033[0m', res)

register()

print()
# https://www.codenong.com/cs109509516/