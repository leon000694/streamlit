print()
import base64

## 加密
def enctry(s):
	k = 'z&sg6nu7A79tP#g#a6Q@&1UejtVo^&ys*SH^sOtTW*!WiUGmS19L#j%3daBBFs!IlvS*!9u3Ht@qKVum'
	encry_str = ''
	for i, j in zip(s, k): # i為字符,j為密鑰字符
		temp = str(ord(i)+ord(j))+'_' # 加密字符=字符的unicode碼+密鑰的unicode碼
		encry_str = encry_str +temp
	enc_str = base64.b64encode(encry_str.encode('utf-8'))
	return enc_str

data = input("請輸入要加密密碼:")
enc_str = enctry(data)
print("加密後數據為:", enc_str, '\n')


# k = 'z&sg6nu7A79tP#g#a6Q@&1UejtVo^&ys*SH^sOtTW*!WiUGmS19L#j%3daBBFs!IlvS*!9u3Ht@qKVum'
# 教學: https://dragongo.co/%E7%94%A8python%E5%B0%87%E8%87%AA%E5%B7%B1%E7%9A%84%E5%AF%86%E7%A2%BC%E5%8A%A0%E5%AF%86%E8%88%87%E8%A7%A3%E5%AF%86/