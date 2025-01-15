import pygame
import math
import random
# setting up the conststnntds
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_STARTING_X_POSITION_OR_COORDINADES = 0
PLAYER_STARTING_Y_POSITION_OR_COORDINADES = 0
ENEMYSTARTYMIN = 50
ENEMYSTARTYMAX = 200
ENEMYVELOCITY_Y = 10
ENEMYVELOCITYX = 5
BULLETSPEEDY = 50
COLLISION_DISTANCE = 5
pygame.init()
runnin = True
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load('ssbg.png')
pygame.display.set_caption("Space Shooter 2013 (pirated version)")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
PLAYER_IMAGE = pygame.image.load('Player.png')
playerx = PLAYER_STARTING_X_POSITION_OR_COORDINADES
playery = PLAYER_STARTING_Y_POSITION_OR_COORDINADES
PLAYER_X_CHANGE = 0
PLAYER_Y_CHANGE = 0
ENEMY_IMAGE = []
ENEMYX = []
ENEMY_Y = []
ENEMY_X_CHANGE = []
ENEMY_Y_CHANGE = []
ENEMY_AMOUNT_MAX = 10
for i in range(ENEMY_AMOUNT_MAX):
    ENEMY_IMAGE.append(pygame.image.load('enemy.png'))
    ENEMYX.append(random.randint(0,SCREEN_WIDTH-100))
    ENEMY_Y.append(random.randint(ENEMYSTARTYMIN, ENEMYSTARTYMAX))
    ENEMY_X_CHANGE.append(ENEMYVELOCITYX)
    ENEMY_Y_CHANGE.append(ENEMYVELOCITY_Y)
while runnin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin = False