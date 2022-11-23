import pygame
pygame.init()
from pygame.draw import *

FPS = 30
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))

#####

circle(screen, (255, 255, 0), (250, 250), 100) #head
circle(screen, (0, 0, 0), (250, 250), 100, 1)

circle(screen, (255, 0, 0), (210, 220), 20) #eyes
circle(screen, (255, 0, 0), (500-210, 220), 20)
circle(screen, (0, 0, 0), (210, 220), 10)
circle(screen, (0, 0, 0), (500-210, 220), 10)

polygon(screen, (0, 0, 0), [[200, 185], [210, 185], [235, 215], [235, 215]]) #eyebrows
polygon(screen, (0, 0, 0), [[500-200, 185], [500-210, 185], [500-235, 215], [500-235, 215]])

rect(screen, (0, 0, 0), (200, 280, 100, 20)) #mouth
#####

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
