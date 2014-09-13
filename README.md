PyGame-Tile-Game
================
Adam Simone

final version of PyGame game, written in 2013

Project focuses heavily of tile engine functionality, features include:

Tile engine generates semi-random world, dynamically add border tiles from neighboring tiles.
Character can select and change individual tiles during play, inspired by Minecraft.
World map supports multiple tiles in single slot, used for alpha layers to stack tiles with transparent parts.
foreground tiles rendered after player. Player can walk behind tree with alpha layer while still on top of grass tile underneath. 

Other notable areas of work in project:


8 way directional character movement.
Inventory system.
NPC have state stack to change an enemy's mode for instance, chasing the player or being attacked. Different entities can change each other's state to interact. 
All pixel art was done by myself in gimp.
