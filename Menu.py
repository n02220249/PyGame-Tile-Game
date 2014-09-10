import pygame, sys, math
from pygame import *
from math import *
class Menu(pygame.sprite.Sprite):

    def __init__(self, image, image2 ,screen, background):
        pygame.sprite.Sprite.__init__(self)
	self.done = False
	self.image = image
	self.screen = screen
	self.button1 = Button(404, 230, self.image, self, 0)
	self.button2 = Button(404, 300, image2, self, 1)
   	self.buttonsprite = pygame.sprite.Group()
	self.buttonsprite.add(self.button1)
	self.buttonsprite.add(self.button2)
	self.mouseX = 0
	self.mouseY = 0
	self.mouseClickX = 0
	self.mouseClickY = 0
	self.background = background

    def eventHandler(self):
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEMOTION:
			print "JJJJJJ"
			x, y = event.pos
			self.mouseX = x
			self.mouseY = y
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x, y = event.pos
			self.mouseClickX = x
			self.mouseClickY = y
		if event.type == KEYDOWN:
			if event.key == K_p:
				self.done = True
	
    def runMenu(self):
	
	while self.done == False:
		self.eventHandler()
		self.buttonsprite.update(self.mouseX, self.mouseY, self.mouseClickX, self.mouseClickY)
		self.mouseClickX = 0
		self.mouseClickY = 0	
		print "QQQ"
		self.draw(self.screen)
		self.buttonsprite.draw(self.screen)
   		pygame.display.update()
    def setDone(self, value):
	self.done = value

    def draw(self, surface):
	surface.blit(self.background, (372,200))


import math
class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, image, menu, type):
        pygame.sprite.Sprite.__init__(self)
        self.rect = image.get_rect()
	self.image = image
	self.rect.topleft = (x,y)
	self.t = (-math.pi/2)
	(self.x, self.y) = self.rect.topleft
	self.menu = menu
	self.type = type


    def update(self, mouseX, mouseY, mouseClickX, mouseClickY):
	collide1 = self.rect.collidepoint(mouseClickX, mouseClickY)
	if collide1 == True:
		print "VVVVVV"
		if self.type == 0:
			self.menu.setDone(True)
		if self.type == 1:
			pygame.quit()
			sys.exit()
	collide2 = self.rect.collidepoint(mouseX, mouseY)
	if collide2 == True:
		print "Touch"
		self.bounce()


    def bounce(self):

	self.y = self.y + sin(self.t)/4
	
	print sin(self.t)
	self.t = self.t + math.pi/20
	self.rect.topleft = (self.x, self.y)


