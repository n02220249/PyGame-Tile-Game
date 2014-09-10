import pygame, sys
from pygame import *

class InputHandler():

    def __init__(self, spritegroup, playersprite, entitysprite, enemysprite, inv, player, debugger, pauseMenu):
	pygame.init()
	self.mapsprite = spritegroup
	self.playersprite = playersprite
	self.entitysprite = entitysprite
	self.enemysprite = enemysprite
	self.inv = inv
	self.dx, self.dy = 0, 0
	self.player = player
	self.debugger = debugger
	self.pauseMenu = pauseMenu
	
    def save(self):
	print "save"
	#self.player.update(105)
	sprites = self.mapsprite.sprites()
	sprites.sort(key = lambda x: x.x)		#secondary sort
	sprites.sort(key = lambda x: x.y)		#primary sort

	prevTile = sprites[0]

	lineString = "[level]\nmap = "
	firstFlag = 1
	for tiles in sprites:
		
		if (tiles.y == prevTile.y and tiles.x == prevTile.x and tiles != sprites[0]):
			

			lineString = lineString + "," + str(tiles.getID())
		#	if (tiles.x == currentx and tiles != sprites[0]):
		#		lineString = lineString + ","
		#	else:
		#		lineString = lineString + "}{"
		#		currentx = tiles.x
		else:
			print "SSS"
			if (prevTile.y != tiles.y):
				lineString = lineString + "}\n      {" + str(tiles.getID())
				firstFlag = 0
			elif (firstFlag == 1):
				firstFlag = 0
				lineString = lineString +"{"+ str(tiles.getID())	
			elif (tiles == sprites[len(sprites)-1]):
				lineString = lineString + "}{" + str(tiles.getID()) +"}"
			else:
				lineString = lineString + "}{"  + str(tiles.getID())

			prevTile = tiles
	
	f = open('level.txt','wt')
	f.write(lineString)	
	f.close()	
	print lineString
	for tiles in sprites:
		print tiles.y


    def poll(self):
	
    	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:		
			if event.key == K_p:
				self.pauseMenu.runMenu()
				self.pauseMenu.setDone(False)	
		if self.player.getMode() == '0':
		
			if event.type == KEYUP:
				if event.key ==K_LEFT:
						self.dx = 0
						self.mapsprite.update(5)
						self.entitysprite.update(5)
						self.enemysprite.update(5)

				elif event.key == K_RIGHT:
						self.dx = 0
						self.mapsprite.update(5)
						self.entitysprite.update(5)
						self.enemysprite.update(5)
				elif event.key ==K_UP:
						self.dy = 0
						self.mapsprite.update(6)
						self.entitysprite.update(6)
						self.enemysprite.update(6)	
		
				elif event.key == K_DOWN:
						self.dy = 0
						self.mapsprite.update(6)
						self.entitysprite.update(6)
						self.enemysprite.update(6)

			if event.type == KEYDOWN:
					if event.key == K_i:
						self.inv.toggleDraw()
					if event.key == K_d:
						self.inv.attemptCursorLeft()
					if event.key == K_a:
						self.playersprite.update(101)
					if event.key == K_d:
						self.debugger.toggleDraw()
					if event.key == K_l:
						print "%%%%%"
						self.player.update(105)
					if event.key == K_s:
						self.save()
					if pygame.key.get_pressed()[K_LEFT]:	
						self.dx = -1		
						self.mapsprite.update(1)
						self.entitysprite.update(1)
						self.enemysprite.update(1)
		
			
	print pygame.key.get_pressed()[K_LEFT]
	if pygame.key.get_pressed()[K_LEFT]:	
			self.dx = -1		
			self.mapsprite.update(1)
			self.entitysprite.update(1)
			self.enemysprite.update(1)	

	if pygame.key.get_pressed()[K_RIGHT]:
		self.dx = 1	
		self.mapsprite.update(2)
		self.entitysprite.update(2)
		self.enemysprite.update(2)

	if pygame.key.get_pressed()[K_UP]:
		self.dy = -1	
		self.mapsprite.update(3)
		self.entitysprite.update(3)
		self.enemysprite.update(3)


			
	if pygame.key.get_pressed()[K_DOWN]:
		self.dy = 1	
		self.mapsprite.update(4)
		self.entitysprite.update(4)
		self.enemysprite.update(4)
#	if pygame.key.get_pressed()[K_l]:
#		print "MMM" 
#		self.mapsprite.update(105)

	if self.player.getMode() == '1' or self.player.getMode() == '2' or self.player.getMode() == '3':
		self.mapsprite.update(5)
		self.entitysprite.update(5)
		self.enemysprite.update(5)
		self.mapsprite.update(6)
		self.entitysprite.update(6)
		self.enemysprite.update(6)



	
						
        if self.dx > 0 and self.dy > 0:   self.playersprite.update(5)
        if self.dx > 0 and self.dy < 0:   self.playersprite.update(6)
        if self.dx < 0 and self.dy > 0:   self.playersprite.update(7)
        if self.dx < 0 and self.dy < 0:   self.playersprite.update(8)

        if self.dx == 0 and self.dy > 0:  self.playersprite.update(4)
        if self.dx == 0 and self.dy < 0:  self.playersprite.update(3)
        if self.dx < 0 and self.dy == 0:  self.playersprite.update(1)
        if self.dx > 0 and self.dy == 0:  self.playersprite.update(2)