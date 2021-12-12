print()

""" 轉十系列 """
def bin2dec1(s): # 用函數解法
	print(int(s, 2))
	print()
	return
#bin2dec('1101010') # 106

def bin2dec2(b): # 用原理解法
	res = 0
	for d in b:
		res *= 2
		res += int(d)
	print('res1=', res)
	print()
#bin2dec2('1101010') #106
	
def bin2dec3(b): #
	sum = 0
	for n, v in enumerate(reversed(b)):
		sum += int(v)*2**n
		print(n, v, res)
	print()
#bin2dec3('1101010') #106

#any轉十
def myint(s, base=10): # 通用解法
	table ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' #讓各進位索引出所對應之數值，如E為16進位之14
	res = sum(table.index(v)*base**n for n, v in enumerate(reversed(s)))
	print(res)
	return 
myint('E', 16)
#myint('11001', 2)
#myint('1024')


""" 轉二系列 """
print(bin(106))                #  十轉二
print(bin(int('0x3f2a1', 16))) #十六轉二
print(bin(int('125', 8)))      #  八轉二


""" 轉十六系列 """
print(hex(int('1101010'))) # 二轉十六

print()