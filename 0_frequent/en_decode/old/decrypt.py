print()
import base64

## 解密
def dectry(s):
	p = base64.b64decode(s).decode('utf-8')
	k = 'z&sg6nu7A79tP#g#a6Q@&1UejtVo^&ys*SH^sOtTW*!WiUGmS19L#j%3daBBFs!IlvS*!9u3Ht@qKVum'
	dec_str = ""
	for i, j in zip(p.split("_")[:-1], k): # i為加密字符，j為密鑰字符
		temp = chr(int(i)-ord(j)) # 解密字符=(加密unicode碼字符-密鑰字符unicode碼)的單字節字符
		dec_str = dec_str + temp
	return dec_str

#dec_str = dectry('')


# 教學: https://dragongo.co/%E7%94%A8python%E5%B0%87%E8%87%AA%E5%B7%B1%E7%9A%84%E5%AF%86%E7%A2%BC%E5%8A%A0%E5%AF%86%E8%88%87%E8%A7%A3%E5%AF%86/