import pygame
pygame.init()
screen = pygame.display.set_mode((480,360))
runnin = True
screen.fill("white")
pygame.draw.circle(screen, "black", (240, 100),50)
pygame.display.flip()
pygame.draw.circle(screen, "gray", (300, 100),50)
pygame.display.flip()
while runnin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin = False