# Importing the modules
import pygame
import random
# initializing pygame
pygame.init()
SPRITECLR_EVENT = pygame.USEREVENT+1
BGCLR_EVENT = pygame.USEREVENT+1
# selecting the bg colours..
BLUE = pygame.Color('blue')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
PINK = pygame.Color('pink')
# selecting the sprite colors..
SBLUE = pygame.Color('blue')
SRED = pygame.Color('red')
SGREEN = pygame.Color('green')
SPINK = pygame.Color('pink')
# Creating a sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        # Create sprite surface with a demise and color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary = True
        if boundary: 
            pygame.event.post(pygame.event.Event(SPRITECLR_EVENT))
            pygame.event.post(pygame.event.Event(BGCLR_EVENT))
    def CC(self):
        self.image.fill(random.choice([SRED, SBLUE, SGREEN, SPINK]))
def BGC(self):
    global bgcolor
    bgcolor = random.choice([BLUE, RED, GREEN, PINK])
g = pygame.sprite.Group()
spr1 = Sprite(PINK, 20, 20)
spr1.rect.x = random.randint(0,480)
spr1.rect.y = random.randint(0,360)
g.add(spr1)
screen = pygame.display.set_mode((500,400))
runnin = True
bgcolor = BLUE
screen.fill(bgcolor)
clock = pygame.time.Clock()
while runnin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin = False
        elif event.type == SPRITECLR_EVENT:
            spr1.CC()
        elif event.type == BGCLR_EVENT:
            BGC()
    g.update()
    screen.fill(bgcolor)
    g.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()