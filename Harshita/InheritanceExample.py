class Rectangle():
	def __init__(self,leng,br):
		self.length = leng
		self.breadth = br
	
	def area(self):
		return self.length*self.breadth
	def perimeter(self):
		print("perimeter of rectangle is :" ,(2*(self.length+self.breadth)))
		
class Square(Rectangle):
	def __init__(self,side):
		Rectangle.__init__(self,side,side)
		self.side = side
	def perimeter(self):
	    Rectangle.perimeter(self)
		print("perimeter of square is :", (4*self.side))
s = Square(4)
print (s.length)
print (s.breadth)
print (s.side)
print (s.area())
s.perimeter()