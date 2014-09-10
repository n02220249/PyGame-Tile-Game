from random import randint
class TerrainGenerator():
	
	def __init__(self, file, size_x, size_y):
		self.file = file
		self.size_x = size_x
		self.size_y = size_y
		self.map = [[['0' for x in xrange(1)] for x in xrange(size_x)] for x in xrange(size_x)] 
	def generate(self):
	#	self.genRandPoints(5)
	#	self.test()
	#	self.createLakes()
	#	self.createTree(4,4)
	#	self.createTree(4,5)
		self.forest()
		self.beach()
		self.ocean()
		self.map[7][7].remove('0')
		self.map[7][7].append('6')

		self.map[8][7].remove('0')
		self.map[8][7].append('6')

		self.map[7][6].remove('0')
		self.map[7][6].append('6')

		self.border()
		self.map[10][10].remove('0')
		self.map[10][10].append('1')
		self.map[10][10].append('11')
		self.map[10][10].append('12')


		self.map[10][11].append('14')
		self.writeToFile()


	def forest(self):
		for a in range(1, 6):		#hor
			for b in range(1, 30):	#ver
				self.createTree(a,b)
	def beach(self):
		for a in range(20, 25):		#hor
			for b in range(1, 29):	#ver
				if '0' in self.map[b][a]:	
					self.map[b][a].remove('0')
				self.map[b][a].append('13')
	def ocean(self):
		for a in range(25, 30):		#hor
			for b in range(1, 29):	#ver
				if '0' in self.map[b][a]:	
					self.map[b][a].remove('0')
				self.map[b][a].append('1')
	def border(self):
		for point_x in range(0, len(self.map[0])):
			for point_y in range(0, len(self.map)):

				if '6' in self.map[point_y][point_x] or '13' in self.map[point_y][point_x]:		# if dirt

					if '0' in self.map[point_y-1][point_x] or '5' in self.map[point_y-1][point_x]:		# top
						self.map[point_y][point_x].append(10)

					if '0' in self.map[point_y][point_x+1] or '5' in self.map[point_y][point_x+1]:		# top
						self.map[point_y][point_x].append(9)

					if '0' in self.map[point_y+1][point_x] or '5' in self.map[point_y+1][point_x]:		# top
						self.map[point_y][point_x].append(8)

					if '0' in self.map[point_y][point_x-1] or '5' in self.map[point_y][point_x-1]:		# top
						self.map[point_y][point_x].append(7)

	def genRandPoints(self, amount):
 		for t in range(0, amount):
			x = randint(0,self.size_x-1)
			y = randint(0,self.size_y-1)
			self.map[y][x] = 2

	def createTree(self, x, y):

		self.map[y-1][x].append('4')	#top of tree
		if '0' in self.map[y][x]:
			self.map[y][x].remove('0')
		self.map[y][x].append('5')



	def createLakes(self):
		for point_x in range(0, len(self.map[0])):
			for point_y in range(0, len(self.map)):
				if self.map[point_y][point_x] == 2:
					self.lake1(point_y, point_x)
	def lake1(self, base_y, base_x):
		if base_y +3 < len(self.map) and base_x +4 < len(self.map[0]) and base_y - 1 >= 0 and base_x -1 >= 0:

			self.map[base_y][base_x] = 0		# /
			self.map[base_y][base_x+2] = 1		# 2	   0123
			self.map[base_y][base_x+1] = 1		# 1	  
			self.map[base_y+1][base_x+2] = 1	# 5	0   12
			self.map[base_y+1][base_x+1] = 1	# 4	1  3456
			self.map[base_y+2][base_x+2] = 1	# 9	2  789a
			self.map[base_y+2][base_x+1] = 1	# 8	3   bc
			self.map[base_y+3][base_x+2] = 1	# c
			self.map[base_y+3][base_x+1] = 1	# b
			self.map[base_y+1][base_x] = 1		# 3
			self.map[base_y+2][base_x] = 1		# 7
			self.map[base_y+1][base_x+3] = 1	# 6
			self.map[base_y+2][base_x+3] = 1	# a



	def writeToFile(self):	
  		out_file = open("level.txt", "wt")
 		out_file.write("[level]\n")
  		for rows in range(0, len(self.map)):
			for items in range(0, len(self.map[rows])):
				self.map[rows][items] = ','.join(str(e) for e in self.map[rows][items])
			

			str2 = ''.join(str(e) for e in self.map[rows][items])

			if rows == 0:
				
				str1 = '}{'.join(str(e) for e in self.map[rows])

				out_file.write("map = " + "{"+str1 + "}")
				out_file.write("\n")
			else:
				indent = '      '
				str1 = '}{'.join(str(e) for e in self.map[rows])
				out_file.write(indent  + "{"+str1 + "}")
				out_file.write("\n")
  		out_file.close()


t = TerrainGenerator("level.txt", 30, 30)
t.generate()