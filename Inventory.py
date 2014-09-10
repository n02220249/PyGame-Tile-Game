import pygame

class Inv():

   def __init__(self, x, y, menuimage, table, player):
	self.x = x
	self.y = y
        image = pygame.image.load(menuimage).convert_alpha()
	self.table = table
	self.image = image
	self.togdraw = False
	self.player = player
	self.font = pygame.font.SysFont("monospace", 12)

	self.list = []
	self.cursor = 0

   def draw(self, surface):

	if self.togdraw == True:				#only if menu is visible

		if self.cursor == len(self.list):		#roll over from end to 0 for cursor
			self.cursor = 0

		surface.blit(self.image, (self.x,self.y))	# draw menu background

		if len(self.list) > 0:


			if self.list[self.cursor][0] == 14: #!= null		# first part of idpackage is number id, second is string id

				self.titleText = self.font.render(self.list[self.cursor][1], True, (0, 0, 0))  #text
				surface.blit(self.titleText, (self.x+26,self.y+22))
		
		x = 0									
		for items in self.list:				# place cursor background and images
			if x == self.cursor:
				surface.blit(self.table[55], (self.x + (34*x) + 25,self.y + 48))
			surface.blit(self.table[items[0]], (self.x + (34*x) + 25,self.y + 48))
			x = x + 1



   def toggleDraw(self):
	if self.togdraw == True:
		self.togdraw = False
	else:
		self.togdraw = True

   def add(self, id, strID):
	idtuple = (id, strID)
	self.list.append(idtuple)
	print self.list

   def attemptCursorLeft(self):
	if self.togdraw == True:
		self.cursor = self.cursor + 1

   # def attemptDropatCursor():
	
