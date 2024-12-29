import pygame
pygame.init()
screen = pygame.display.set_mode((480,360))
runnin = True
while runnin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin = False
    pygame.draw.rect(screen, "white", pygame.Rect(100,100,100, 50))
    pygame.display.flip()
    pygame.draw.rect(screen, "white", pygame.Rect(300,100,100, 50))
    pygame.display.flip()