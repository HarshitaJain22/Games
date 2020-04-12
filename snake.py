import pygame
import random
 
pygame.init()
 
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake (hisssssssssssss)")
 
run = True
 
head_x = 80
head_y = 100
 
body_1x = 60
body_1y = 100

body_2x = 60
body_2y = 100

fps = 1
clock = pygame.time.Clock()
 
velocity_x = 0
velocity_y = 0

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


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
 
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

                 
    make_grid()
    body_2x = body_1x
    body_2y = body_1y
    body_1x = head_x
    body_1y = head_y
    head_x += velocity_x
    head_y += velocity_y
    head_pos = [head_x, head_y]
    pygame.draw.rect(window, (0, 255,0) , (head_x, head_y, 20, 20))
    pygame.draw.rect(window, (0, 0,0) , (head_x+4, head_y+4, 12,12))
    pygame.draw.rect(window, (0, 255,0) , (body_1x, body_1y, 20, 20))
    pygame.draw.rect(window, (0, 255,0) , (body_2x, body_2y, 20, 20))
    pygame.display.update()
    clock.tick(fps)
 
 
pygame.quit()
