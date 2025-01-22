# take a wild guess what this does
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
# creaaated screeyn
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load('ssbg.png')
# caption
pygame.display.set_caption("Space Shooter 2013 (pirated version)")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
# playiemasge
PLAYER_IMAGE = pygame.image.load('Player.png')
playerx = PLAYER_STARTING_X_POSITION_OR_COORDINADES
playery = PLAYER_STARTING_Y_POSITION_OR_COORDINADES
PLAYER_X_CHANGE = 0
PLAYER_Y_CHANGE = 0
# omg its the anamy
ENEMY_IMAGE = []
ENEMYX = []
ENEMY_Y = []
ENEMY_X_CHANGE = []
ENEMY_Y_CHANGE = []
# crreating 10 enemys
ENEMY_AMOUNT_MAX = 10
for i in range(ENEMY_AMOUNT_MAX):
    ENEMY_IMAGE.append(pygame.image.load('enemy.png'))
    ENEMYX.append(random.randint(0,SCREEN_WIDTH-100))
    ENEMY_Y.append(random.randint(ENEMYSTARTYMIN, ENEMYSTARTYMAX))
    ENEMY_X_CHANGE.append(ENEMYVELOCITYX)
    ENEMY_Y_CHANGE.append(ENEMYVELOCITY_Y)
# while runnin:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             runnin = False
BULLET_IMAGE = pygame.image.load('bullet.png')
BULLET_X = 0
BULLET_Y = PLAYER_STARTING_Y_POSITION_OR_COORDINADES
BULLET_X_CHANGE = 0
BULLET_Y_CHANGE = BULLETSPEEDY
# SCORE = 0!!!!!!!
SCORE = 0
TEXTX = 50
TEXTY = 50
def showscore(x, y):
    screen.blit(SCORE, (x,y))
def speedblitzdropkick(x,y):
    screen.blit('gameover you got speedbliutz drop kicke d ', (x,y))
def player(x,y):
    screen.blit(PLAYER_IMAGE, (x,y))
def enemy(x,y,i):
    screen.blit(ENEMY_IMAGE[i], (x,y))
def bulletfiresohno(x,y):
    global BULLET_STATE
    BULLET_STATE = 'fire'
    screen.blit(BULLET_IMAGE, (x+15, y+15))
def iscollide(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx-bulletx)**2, (enemyy-bullety)**2)
    return distance < COLLISION_DISTANCE
while runnin:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER_X_CHANGE = -5
            if event.key == pygame.K_RIGHT:
                PLAYER_X_CHANGE = 5
            if event.key == pygame.K_SPACE and BULLET_STATE == 'Ready!':
                BULLET_X = playerx
                bulletfiresohno(BULLET_X,BULLET_Y)
        if event.type == pygame.K_UP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            PLAYER_X_CHANGE = 0
        playerx+= PLAYER_X_CHANGE
        playerx = max(0,min(playerx,SCREEN_WIDTH))
        for i in range(ENEMY_AMOUNT_MAX):
            if ENEMY_Y[i] > 340:
                for j in range(ENEMY_AMOUNT_MAX):
                    ENEMY_Y[j] = 2000
                speedblitzdropkick(0,0)
                break
            ENEMYX[i] += ENEMY_X_CHANGE[i]
player(playerx, playery)
pygame.display.update()
