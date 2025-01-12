import pygame
import random
pygame.init()
runnin = True
movementvelocity = 5
fontsize = 70
bgimg = pygame.transform.scale(pygame.image.load("crimson every ai you open.png"),(500,500))
font = pygame.font.SysFont("Comic Sans MS", fontsize)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("black"))
        pygame.draw.rect(self.image, color, pygame.Rect(0,0, width,height))
        self.rect = self.image.get_rect()
    def move(self, x, y):
        self.rect.x = max(min(self.rect.x+x, 500-self.rect.width), 0)
        self.rect.y = max(min(self.rect.y+y, 500-self.rect.height), 0)
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Spriet collisio n wow cool omg")
allsprite = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color("red"), 50,50)
sprite1.rect.x, sprite1.rect.y = random.randint(0,500- sprite1.rect.width), random.randint(0,500- sprite1.rect.height)
allsprite.add(sprite1)
sprite2 = Sprite(pygame.Color("blue"), 50,50)
sprite2.rect.x, sprite2.rect.y = random.randint(0,500- sprite2.rect.width), random.randint(0,500- sprite2.rect.height)
allsprite.add(sprite2)
win = False
clock = pygame.time.Clock()
while runnin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            runnin = False
        if not win:
            keys = pygame.key.get_pressed()
            x = (keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*movementvelocity
            y = (keys[pygame.K_DOWN]-keys[pygame.K_UP])*movementvelocity
            sprite1.move(x,y) 
            if sprite1.rect.colliderect(sprite2.rect):
                allsprite.remove(sprite2)
        screen.blit(bgimg,(0,0))
        pygame.display.flip()
        clock.tick(90)