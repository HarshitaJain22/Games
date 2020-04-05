import pygame
import random

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake (hisssssssssssssssssss)")
pygame.display.update()

run = True
head_x = 60
head_y = 100
fps = 5
clock = pygame.time.Clock()
velocity_x = 0
velocity_y = 0

fruit_x = random.randint(0,500)
fruit_y = random.randint(0,500)

fcentre_x = (20*(fruit_x//20))+10
fcentre_y = (20*(fruit_x//20))+10

if (fcentre_x == head_x) or (fcentre_y == head_y):
    fruit_x = random.randint(0,500)
    fruit_y = random.randint(0,500)
    fcentre_x = 20*(fruit_x//20)
    fcentre_y = 20*(fruit_x//20)


def make_grid():
    window.fill((255,255,255))
    diff = 20
    x = 0
    y = 0
    for i in range (0,25):
        x = x + diff
        y = y + diff
        pygame.draw.line(window, (0,0,0), (x,0), (x,500))
        pygame.draw.line(window, (0,0,0), (0,y), (500,y))
        pygame.display.update()

make_grid()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 20
                velocity_y = 0
                
            if event.key == pygame.K_LEFT:
                velocity_x = -20
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -20

            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = 20
    #window.fill((0,0,0))            
    #make_grid()
    head_x += velocity_x
    head_y += velocity_y
    pygame.draw.rect(window, (0, 255,0) , (head_x, head_y, 20, 20))
    pygame.draw.circle(window, (255,0,0), (fcentre_x, fcentre_x), 10)
    clock.tick(fps)
    pygame.display.update()


pygame.quit()
