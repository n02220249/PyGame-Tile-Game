import pygame, sys, ConfigParser
from pygame.locals import *
from Tile1 import *
from Player1 import *
from Entity import *
from InputHandler import *
#from TerrianGenerator import *
from Inventory import *
from Enemy import *
from Debugger import *
from Menu import *
from random import randint

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert_alpha()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_y in range(0, image_height/height):
    	for tile_x in range(0, image_width/width):	
    		rect = (tile_x*width, tile_y*height, width, height)
    		tile_table.append(image.subsurface(rect))
    return tile_table


def loadMap():

   parser = ConfigParser.ConfigParser()
   parser.read("level.txt")

   map = parser.get('level', 'map').split("\n")
   print len(map)
   for rows in range(len(map)):
   	map[rows] = ''.join(map[rows]).split("}")

	for i in range(len(map[rows])):

		map[rows][i] = map[rows][i][1:]
#		if ',' in map[rows][i]:
		map[rows][i] = map[rows][i].split(",")

	map[rows].pop(-1)


   return map	

def createMapSprites(x , y, map, table):
   mapsprite = pygame.sprite.Group()
   mapblockedsprite = pygame.sprite.Group()
   backoverlaysprite = pygame.sprite.Group()
   frontoverlaysprite = pygame.sprite.Group()
   for tile_x in range(0, len(map[0])):
	for tile_y in range(0, len(map)):
		print "$$$"
		print map[tile_y][tile_x]
		for items in range(len(map[tile_y][tile_x])):
			if map[tile_y][tile_x][items] == '0':
				tile = Tile(tile_x*32, tile_y*32, table[0], 0)
			if map[tile_y][tile_x][items] == '1':
				tile = Tile(tile_x*32, tile_y*32, table[1], 1)
				mapblockedsprite.add(tile)
			if map[tile_y][tile_x][items]  == '2':
				tile = Tile(tile_x*32, tile_y*32, table[2], 2)
				mapblockedsprite.add(tile)
			if map[tile_y][tile_x][items]  == '3':
				tile = Tile(tile_x*32, tile_y*32, table[3], 3)
			if map[tile_y][tile_x][items]  == '4':
				tile = Tile(tile_x*32, tile_y*32, table[4], 4)
				frontoverlaysprite.add(tile)
			if map[tile_y][tile_x][items]  == '5':
				tile = Tile(tile_x*32, tile_y*32, table[5], 5)	
				mapblockedsprite.add(tile)
			if map[tile_y][tile_x][items]  == '6':
				tile = Tile(tile_x*32, tile_y*32, table[6], 6)
#				backoverlaysprite.add(tile)
			if map[tile_y][tile_x][items]  == '7':
				tile = Tile(tile_x*32, tile_y*32, table[7], 7)
				backoverlaysprite.add(tile)
			if map[tile_y][tile_x][items]  == '8':
				tile = Tile(tile_x*32, tile_y*32, table[8], 8)
				backoverlaysprite.add(tile)
			if map[tile_y][tile_x][items]  == '9':
				tile = Tile(tile_x*32, tile_y*32, table[9], 9)
				backoverlaysprite.add(tile)
			if map[tile_y][tile_x][items]  == '10':
				tile = Tile(tile_x*32, tile_y*32, table[10], 10)
				backoverlaysprite.add(tile)
			if map[tile_y][tile_x][items]  == '11':
				tile = Tile(tile_x*32, tile_y*32, table[11], 11)
				backoverlaysprite.add(tile)
			if map[tile_y][tile_x][items]  == '12':
				tile = Tile(tile_x*32, tile_y*32, table[12], 12)
				backoverlaysprite.add(tile)
			if map[tile_y][tile_x][items]  == '13':
				tile = Tile(tile_x*32, tile_y*32, table[13], 13)
			if map[tile_y][tile_x][items]  == '14':
				tile = Tile(tile_x*32, tile_y*32, table[14], 14)
				backoverlaysprite.add(tile)
			mapsprite.add(tile)


		result = (mapsprite, mapblockedsprite, backoverlaysprite, frontoverlaysprite) 
   return result

def createPlayerSprite(x, y, playerTable):
   playersprite = pygame.sprite.Group()
   player = Player(x,y, playerTable, enemysprite, mapsprite, table)
   playersprite.add(player)
   return playersprite

def collisionResponse():


# collision with tiles

    collist2 = pygame.sprite.groupcollide(enemysprite, mapblockedsprite, False, False)
#    if len(collist2) > 0:
#	print collist2

    collist = pygame.sprite.spritecollide(player, mapblockedsprite, False)
    if len(collist) > 0:
	for sprites in collist:
		# not statements prevent from getting stuck when sliding across multiple adjacent tiles

		if sprites.rect.right == player.rect.left+1 and sprites.rect.top != player.rect.bottom-1 and sprites.rect.bottom != player.rect.top + 1:
	
			mapsprite.update(7)     #left of player
			entitysprite.update(7)
			enemysprite.update(7)

		if sprites.rect.left == player.rect.right-1 and sprites.rect.top != player.rect.bottom-1 and sprites.rect.bottom != player.rect.top + 1:

			mapsprite.update(8)	#right of player
			entitysprite.update(8)
			enemysprite.update(8)

		if sprites.rect.top == player.rect.bottom-1 and sprites.rect.right != player.rect.left+1 and sprites.rect.left != player.rect.right-1:

			mapsprite.update(9)	#up of player
			entitysprite.update(9)
			enemysprite.update(9)

		if sprites.rect.bottom == player.rect.top + 1 and sprites.rect.right != player.rect.left+1 and sprites.rect.left != player.rect.right-1:

			mapsprite.update(11)	#down of player
			entitysprite.update(11)
			enemysprite.update(11)


 # collision with entities

    collist = pygame.sprite.spritecollide(player, entitysprite, True)
    if len(collist) > 0:
	print "AAAAAAA"
	for sprites in collist:

		inv.add(sprites.getID(), sprites.getStringID())		#add item to inventory

def ranmap():
  map = [[1 for x in xrange(30)] for x in xrange(30)] 

  for t in range(0, 5):
	x = randint(0,29)
	y = randint(0,29)
	map[y][x] = 0

  for point_x in range(0, len(map[0])):
	for point_y in range(0, len(map)):
		if point_y +1 != len(map) and point_x +1 != len(map[0]) and point_y - 1 >= 0 and point_x -1 >= 0:
			if map[point_y+1][point_x] == 0:
				if randint(1, 100) > 10:
					map[point_y][point_x] = 0
			if map[point_y-1][point_x] == 0:
				if randint(1, 100) > 10:
					map[point_y][point_x] = 0
			if map[point_y][point_x+1] == 0:
				if randint(1, 100) > 10:
					map[point_y][point_x] = 0
			if map[point_y][point_x-1] == 0:
				if randint(1, 100) > 10:
					map[point_y][point_x] = 0
  out_file = open("level.txt", "wt")
  out_file.write("[level]\n")

  for rows in range(0, len(map)):
	if rows == 0:
		str1 = ''.join(str(e) for e in map[rows])
		out_file.write("map = " + str1)
		out_file.write("\n")
	else:
		indent = '      '
		str1 = ''.join(str(e) for e in map[rows])
		out_file.write(indent + str1)
		out_file.write("\n")
  out_file.close()
if __name__=='__main__':
    parser = ConfigParser.ConfigParser()
    parser.read("level.txt")

    test = parser.get('level', 'map')
    print test
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((1000, 700))
    table = load_tile_table("tiletrans4.png", 32, 32)		# create array of tiles
    parser = ConfigParser.ConfigParser()
    parser.read("level.txt")

    test = parser.get('level', 'map')
    print test

    map = loadMap()					# load 2d array of map
    #print map
    x,y = 0,0						# background starting point
    mapsprite, mapblockedsprite, backoverlaysprite, frontoverlaysprite = createMapSprites(x, y, map, table)	# create sprite group for map
    playerTable = load_tile_table("anichar2.png", 32, 32)
    enemyTable = load_tile_table("enemy2.png", 32, 32)






    entitysprite = pygame.sprite.Group()

    entity = Entity(300, 300, 14,"Wood", table[14])						# make wood entity and entity group
    entitysprite.add(entity)

    entity = Entity(500, 300, 14,"Wood", table[14])						# make wood entity and entity group
    entitysprite.add(entity)

    entity = Entity(500, 500, 14,"Wood", table[14])						# make wood entity and entity group
    entitysprite.add(entity)

    enemysprite = pygame.sprite.Group()
    playersprite = createPlayerSprite(500,350, playerTable)	# create sprite group for player
    player = playersprite.sprites()[0]
    
    enemy = Enemy(600, 600,player, enemyTable)
    enemysprite.add(enemy)

    enemy = Enemy(400, 600,player, enemyTable)
    enemysprite.add(enemy)

    inv = Inv(400, 300, "inventory2.png",table, player)
    
    debugger = Debugger(player)
    test = pygame.image.load("background.png").convert_alpha()
    button = pygame.image.load("button.png").convert_alpha()
    button2 = pygame.image.load("buttonExit.png").convert_alpha()
    pauseMenu = Menu(button, button2, screen, test)
    input = InputHandler(mapsprite, playersprite, entitysprite, enemysprite, inv, player, debugger, pauseMenu)


while True:  
    input.poll()			# check input and respond 
    collisionResponse()
    playersprite.update(0) 
    mapsprite.update(0) 		#update map
    entitysprite.update(0)
    enemysprite.update(0)
    mapsprite.draw(screen)		# draw map
    backoverlaysprite.draw(screen)
    player.drawSelTile(screen)
    entitysprite.draw(screen)
    playersprite.draw(screen)		# draw player
    enemysprite.draw(screen)
    frontoverlaysprite.draw(screen)
    inv.draw(screen)
    debugger.draw(screen)
    pygame.display.update()
    fpsClock.tick(60)