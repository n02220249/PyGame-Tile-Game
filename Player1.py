import pygame, sys
from pygame import *
from Animation import *
from Tile1 import *


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, image, enemygroup, mapsprite, tileImage):
	pygame.sprite.Sprite.__init__(self)
	self.foward = Animation(image,0,4, -2)	
 	self.right = Animation(image,8,12, -2)
	self.up = Animation(image, 16, 20, -2)
	self.left = Animation(image, 24, 28, -2)
	self.downright = Animation(image, 28, 32, -2)
	self.downleft = Animation(image, 40, 44, -2)
	self.upright = Animation(image, 48, 52, -2)
	self.upleft = Animation(image, 56, 60, -2)
	self.grabImage = Animation(image, 60, 64, 1)
	self.heldPunchImage = Animation(image, 44, 48, 1)
#	self.selectImage = Animation(image, 37, 41, -2, 1)
	self.tileImage = tileImage
	self.x = x
	self.y = y
	self.list = image
	self.image = self.foward.image()	# default direction facing (right)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)  # update tile rect location
	self.modeStack = []
	self.modeStack.append('0')
	self.enemysprite = enemygroup
	self.z = 0
	self.mapsprite = mapsprite
 	self.selectedTile = Tile(0,0, image,0, mode=1)
	self.tilesprite = pygame.sprite.Group()
	self.tilesprite.add(self.selectedTile)
	self.dirdisX = 0
	self.dirdisY = 0
    
    def drawSelTile(self, screen):
	print "BBBBB"
    	self.tilesprite.draw(screen)

    def swingMode(self):
	
	print "WWWWW"
	self.testImage = self.grabImage.image()
	if self.testImage == -1:
		self.pop()
		collist = pygame.sprite.spritecollide(self, self.enemysprite, False)
		if len(collist) > 0:
			self.enemy = collist[0]
		#	collist[0].push(collist[0].heldMode(self.x+20,self.y+20))
			self.enemy.push('2')
			self.push('2')	
		self.image = self.lastimage
		
	else: self.image = self.testImage


	
    def getX(self):
	return self.x
    def getY(self):
	return self.y 

    def placeBlockMode(self): 
	print "GGGGG"
	print self.selectedTile.rect
	collist = pygame.sprite.spritecollide(self.selectedTile, self.mapsprite, False)
	if len(collist) > 0:
		for tiles in collist:
			print tiles.rect.topleft
			(self.tx,self.ty) = tiles.rect.topleft

			tiles.kill()
#			x = self.x +self.tx
#			y = self.y + self.ty
		tile = Tile(self.selectedTile.getX(), self.selectedTile.getY(), self.tileImage[6], 6)
		self.mapsprite.add(tile)

	self.pop()

    def runMode(self):
	if self.modeStack[0] == '0':
		self.defaultMode()   
    	elif self.modeStack[0] == '1':
		self.swingMode() 
    	elif self.modeStack[0] == '2':
		self.grappleMode() 
    	elif self.modeStack[0] == '3':
		self.throwMode() 
    	elif self.modeStack[0] == '4':
		self.heldPunchMode() 
    	elif self.modeStack[0] == '5':
		self.placeBlockMode() 
    def grappleMode(self):
	self.image = self.list[52]
	if pygame.key.get_pressed()[K_q]:    #if q enter throw
		self.push('3')
	if pygame.key.get_pressed()[K_w]:    #if q enter punch
		self.push('4')
		self.enemy.push('3')

    def push(self, mode):
	self.modeStack.insert(0, mode)
    def throwMode(self):
	print "throw"
	# (self.x,self.y) = self.rect.topleft
	if self.z == 0:
		self.y = self.y + 4
	if self.z == 1:
		self.y = self.y + 2
	if self.z == 2:
		self.y = self.y - 2
	if self.z == 3:
		self.y = self.y - 4
	if self.z == 4:
		self.pop()
		self.z = 0

	self.z = self.z + 1
	self.rect.topleft = (self.x,self.y)
    def heldPunchMode(self):
	self.testImage =self.heldPunchImage.image()
	if self.testImage == -1:
		self.pop()
	else: self.image = self.testImage
	print "punch"
    def pop(self):
	self.modeStack.pop(0)
    def defaultMode(self):

	if self.dir == 1:
		self.dirdisX = -26
		self.dirdisY = 16
		self.image = self.left.image()		# left
	elif self.dir == 2:
		self.dirdisX = 60
		self.dirdisY = 16
		self.image = self.right.image()	# right
	elif self.dir == 3:
		self.dirdisX = 16
		self.dirdisY = -26
		self.image = self.up.image()	# up
	elif self.dir == 4:
		self.dirdisY = 60
		self.dirdisX = 16		
		self.image = self.foward.image()	# down

	elif self.dir == 5:
		self.dirdisY = 48
		self.dirdisX = 48
		self.image = self.downright.image()	# down right
	elif self.dir == 6:
		self.dirdisX = 48
		self.dirdisY = -16

		self.image = self.upright.image()	# up right
	elif self.dir == 7:
		self.dirdisX = -16
		self.dirdisY = 48
		self.image = self.downleft.image()	# down left
	elif self.dir == 8:  
		self.dirdisX = -16
		self.dirdisY = -16
		self.image = self.upleft.image()	# up left
	self.lastimage = self.image

	for tiles in self.mapsprite.sprites():
		if tiles.rect.collidepoint(self.x + self.dirdisX, self.y + self.dirdisY) == True:
			print "@@@@@@" 
			self.selectedTile.rect = tiles.rect

    def getMode(self):

	return self.modeStack[0]
    def getSelf(self):
	return self
    def update(self, dir):
	print "JJJJ"

	self.selectedTile.update(0)

	if dir == 101: self.push('1')
	if dir == 102: return self.getMode()
	if dir == 103: return self.getSelf()

	if dir == 104: self.push('3')
	
	if dir == 105: self.push('5')
	print self.selectedTile.rect
	self.dir = dir
	self.runMode()
	
	