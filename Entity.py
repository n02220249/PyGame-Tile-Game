import pygame
from Animation import *


class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y, id, strID, image):
	self.x = x
	self.y = y
        pygame.sprite.Sprite.__init__(self)
	
	# self.imglist = Animation(image,0,5)	

        self.image = image
	self.id = id
	self.strID = strID
	self.dx, self.dy = 0, 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)


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
	self.x += self.dx
	self.y += self.dy

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
		
		self.move()
	#	self.image = self.imglist.image()
