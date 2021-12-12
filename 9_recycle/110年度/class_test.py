# 汽車類別
class Cars:
	# 建構式
	def __init__(self, color, seat):
		self.color = color 
		self.seat = seat 

	# 方法
	def drive(self):
		print(f"My car is {self.color} and {self.seat} seat.")

class Motorcycle:
	pass

mazda = Cars('green', 4)
mazda.drive()