import pygame

class Debugger():

   def __init__(self, player):

	self.togdraw = False
	self.player = player
	self.font = pygame.font.SysFont("monospace", 20)
	self.font.set_bold(True) 


   def draw(self, surface):

	if self.togdraw == True:				#only if menu is visible

		string = "Player Mode:  "
		string = string + self.player.getMode()

		self.titleText = self.font.render(string, True, (255, 255, 255))  #text
		surface.blit(self.titleText, (20,20))



   def toggleDraw(self):
	if self.togdraw == True:
		self.togdraw = False
	else:
		self.togdraw = True

