import pygame, sys 
from Animation import *

class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y, image, id, mode=None):
	self.x = x
	self.y = y
        pygame.sprite.Sprite.__init__(self)
	self.id = id


	if mode == 1:
		self.animation = Animation(image, 32, 39, -2)
		self.image = self.animation.image()
		self.rect = self.image
		self.mode = 1
		print mode
	else:  
       		self.image = image
        	self.rect = self.image.get_rect()
		self.mode = 0

	self.dx, self.dy = 0, 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
	
    def up(self): self.dy = 1
    def down(self): self.dy = -1
    def left(self): self.dx = 1
    def right(self): self.dx = -1
    def stopx(self): self.dx = 0
    def stopy(self): self.dy = 0
    def getX(self): return self.rect.left
    def getY(self): return self.rect.top
    def getID(self): return self.id
# used in collision response

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
	self.x += self.dx
	self.y += self.dy
	if self.mode != 1:
		self.position = (self.x,self.y)
		self.rect.topleft = self.position	# update rect position
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
#		print self.mode
		if self.mode == 1:
			print "MMMMMMMM"
			self.image = self.animation.image()
		self.move()

