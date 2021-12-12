print()
from pandas.core.frame import DataFrame

# 第一種:兩個不同列表轉換數據框
a = [1,2,3,4] #列表a
b = [5,6,7,8]
c = {"a":a, "b":b} #將列表a,b轉換成字典
data = DataFrame(c) #將字典轉換成數據框
#print(data)

# 第二種:將包含不同子列表轉換為數據框
a = [[1,2,3,4],[5,6,7,8]] #包含兩個不同子列表
data = DataFrame(a) #以行為標準寫入
#print(data)

# 轉置
data = data.T
data.rename(columns={0:'a',1:'b'},inplace=True)
print(data)

print()