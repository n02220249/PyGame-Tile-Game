import pygame
from Animation import *
from math import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, player, image):
	self.x = x
	self.y = y
        pygame.sprite.Sprite.__init__(self)
	
	# self.imglist = Animation(image,0,5)	
#	self.heldImage = Animation(image,35, 39, -2)
	self.imagelist = image
        self.image = image[3]
	self.dx, self.dy = 0, 0
	self.movex, self.movey = 0, 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
	self.player = player
	self.modeStack = []

	self.modeStack.append('0')
	self.heldImage = Animation(image, 48, 52, -1)
	self.punchedImage = Animation(image, 40, 44, 1)

    def up(self): self.dy = 1
    def down(self): self.dy = -1
    def left(self): self.dx = 1
    def right(self): self.dx = -1
    def stopx(self): self.dx = 0
    def stopy(self): self.dy = 0

    def getID(self):
	return self.id

    def getStringID(self):
	return self.strID

    def stopLeft(self):
	if self.dx > 0:
		self.dx = 0
    def stopRight(self):
	if self.dx < 0:
		self.dx = 0
    def stopUp(self):
	if self.dy < 0:
		self.dy = 0
    def stopDown(self):
	if self.dy > 0:
		self.dy = 0

    def move(self):


	self.x = self.x + self.dx + self.movex
	self.y = self.y + self.dy + self.movey

	self.position = (self.x,self.y)
	self.rect.topleft = self.position	# update rect position
    def defaultMode(self):
	dx = self.player.getX() - self.x
	dy = self.player.getY() - self.y
	hy = sqrt(dx**2 + dy**2)		# length of hypotenuse

	if hy < 200:				# is within distance
		mag = .8
		if hy == 0: hy = 0.000001
		self.movex = (dx / hy)*mag
		self.movey = (dy / hy)*mag
	else:
		self.movex, self.movey = 0, 0	# else stop

	cos1 = (dy / hy)*-1			# flip y to work with traditional smaller down orientation 
	sin1 = (dx / hy)		


	if sin1 < sin(radians(22.5)) and sin1 > sin(radians(337.5)) and cos1 > 0:		#top 
		self.image = self.imagelist[0]
	elif sin1 > sin(radians(22.5)) and sin1 < sin(radians(67.5)) and cos1 > 0:		#top right
		self.image = self.imagelist[57]
	elif cos1 < cos(radians(67.5)) and cos1 > cos(radians(112.5)) and sin1 > 0:		#right
		self.image = self.imagelist[58]
	elif sin1 < sin(radians(112.5)) and sin1 > sin(radians(157.5)) and cos1 < 0:		#bottom right
		self.image = self.imagelist[59]
	elif sin1 < sin(radians(157.5)) and sin1 > sin(radians(202.5)) and cos1 < 0:		#bottom 
		self.image = self.imagelist[60]
	elif sin1 < sin(radians(202.5)) and sin1 > sin(radians(247.5)) and cos1 < 0:		#bottom left
		self.image = self.imagelist[61]
	elif cos1 > cos(radians(247.5)) and cos1 < cos(radians(292.5)) and sin1 < 0:		#left
		self.image = self.imagelist[62]
	elif sin1 > sin(radians(292.5)) and sin1 < sin(radians(337.5)) and cos1 > 0:		#top left
		self.image = self.imagelist[63]

    def runMode(self):
	# print self.modeStack[0]
	if self.modeStack[0] == '0':
		self.defaultMode()
	if self.modeStack[0] == '1':
		self.heldMode()
	if self.modeStack[0][0] == '2':
		self.heldMode(self.player.getX()+13, self.player.getY()+4)
	if self.modeStack[0] == '3':
		self.punchedMode()
	

    def punchedMode(self):
	self.testImage = self.punchedImage.image()
	if self.testImage == -1:
		self.pop()
	else: self.image = self.testImage

    def push(self, mode):
	self.modeStack.insert(0, mode)


    def pop(self):
	self.modeStack.pop(0)

    def heldMode(self, x, y):
	self.image = self.heldImage.image() 
	print "SSSS"
	self.x = x
	self.y = y
	self.movey = 0
	self.movex = 0

    def update(self, dir):
	if dir == 1:  self.left()
	elif dir == 2:  self.right()
	elif dir == 3:  self.up()
	elif dir == 4:  self.down()
	elif dir == 5:  self.stopx()
	elif dir == 6:  self.stopy()
	elif dir == 7:  self.stopLeft()
	elif dir == 8:  self.stopRight()
	elif dir == 9:  self.stopUp()
	elif dir == 11:  self.stopDown()

	else:
		self.runMode()
		self.move()
	#	self.image = self.imglist.image()
