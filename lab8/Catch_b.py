import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

screen.fill(WHITE)
n = 100

color = [0]*n
x = [0]*n
y = [0]*n
vx = [0]*n
vy = [0]*n
r = [0]*n
vr = [5]*n

def sgn(x):
    if x == 0:
        return 1
    return x/abs(x)

def ball_roll(t, j):
    vx0 = vx[j]
    vy0 = vy[j]
    if (x[j] + r[j] >= 1200) or (x[j] - r[j] <= 0):
        vx0 = -vx0*(randint(5, 20)/10.0)
        x[j] = 600 + (600 - r[j] - 1) * sgn(x[j] + r[j] - 1200)
        if (abs(vx0) > 1000) or (abs(vx0) < 100):
            vx0 = 400*sgn(vx0)
    if (y[j] + r[j] >= 900) or (y[j] - r[j] <= 0):
        vy0 = -vy0*(randint(5, 20)/10.0)
        y[j] = 450 + (450 - r[j] - 1) * sgn(y[j] + r[j] - 900)
        if (abs(vy0) > 1000) or (abs(vy0) < 100):
            vy0 = 400*sgn(vy0)
    x0 = x[j] + t * vx0
    y0 = y[j] + t * vy0
    print(j, vx0, vy0)
    return x0, y0, vx0, vy0


def click(cnt: int):
    x0, y0 = pygame.mouse.get_pos()
    cnt0 = cnt
    for i in range(n):
        if (y0 - y[i]) ** 2 + (x0 - x[i]) ** 2 <= r[i] ** 2:
            cnt0 = cnt + 1
    print(cnt0)
    return cnt0


####
pygame.display.update()
clock = pygame.time.Clock()
finished = False
#new_ball()


cnt = 0

for i in range(n):
    color[i] = (randint(0, 255), randint(0, 255), randint(0, 255))
    x[i], y[i], r[i] = randint(100, 1000), randint(100, 1000), randint(5, 100)
    vx[i], vy[i] = sgn(randint(-1, 1))*randint(200, 600), sgn(randint(-1, 1))*randint(200, 600)


while not finished:
    clock.tick(FPS)
    dt = clock.tick(FPS)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cnt = click(cnt)
    screen.fill(WHITE)

    for i in range(n):
        x[i], y[i], vx[i], vy[i] = ball_roll(dt, i)
        color[i] = ((color[i][0] + 10) % 255, (color[i][1] + 10) % 255, (color[i][2] + 10) % 255)
        if(r[i] > 100) or (r[i] < 0):
            vr[i] = -vr[i]
        r[i] = r[i] + vr[i]
        circle(screen, color[i], (x[i], y[i]), r[i])
    pygame.display.flip()

pygame.quit()