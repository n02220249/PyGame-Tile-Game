import pygame

class Animation():

   def __init__(self, images, initFrame, maxFrame, cycles):
	self.images = images
	self.delayLenInit = 5
	self.delayLen = self.delayLenInit
	self.initFrame = initFrame
	self.currentFrame = self.initFrame
	self.maxFrame = maxFrame
	self. cyclesinit = cycles
	self.cycles = cycles



	
   def image(self):

	image = self.images[self.currentFrame]
	self.delayLen = self.delayLen - 1
	if self.delayLen == 0:
		self.delayLen = self.delayLenInit
		self.currentFrame = self.currentFrame + 1
	if self.currentFrame == self.maxFrame:
		self.currentFrame = self.initFrame
		if self.cycles != -2:
			self.cycles = self.cycles - 1
		if self.cycles == 0:
			self.cycles = self.cyclesinit
			return -1
	return image