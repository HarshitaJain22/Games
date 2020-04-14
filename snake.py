import pygame
import random
 
pygame.init()
 
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake (hisssssssssssss)")
 
run = True
 
head_x = 80
head_y = 100
head_pos = [head_x, head_y] 
body_1x = 60
body_1y = 100
body_1pos = [body_1x, body_1y]
body_2x = 40
body_2y = 100
body_2pos = [body_2x, body_2y]

body_c = [head_pos, body_1pos, body_2pos]

fps = 3
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


def coordinates(bodyco, velx, vely):
    bodyc = bodyco
    bodyc[-1][0] = bodyc[-2][0]
    bodyc[-1][1] = bodyc[-2][1]
    bodyc[-2][0] = bodyc[-3][0]
    bodyc[-2][1] = bodyc[-3][1]
    bodyc[-3][0] += velx
    bodyc[-3][1] += vely
    return bodyc


def draw_body(window, bodycor, velox, veloy):
    body = coordinates(bodycor, velox, veloy)
    pygame.draw.rect(window, (0, 255,0) , (body[2][0], body[2][1], 20, 20))
    pygame.draw.rect(window, (0, 255,0) , (body[1][0], body[1][1], 20, 20))    
    pygame.draw.rect(window, (0, 255,0) , (body[0][0], body[0][1], 20, 20))
    pygame.draw.rect(window, (0, 0,0) , (body[0][0]+4, body[0][1]+4, 12,12))
    


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
    draw_body(window, body_c, velocity_x, velocity_y)
    pygame.draw.rect(window, (0, 0,255) , (head_x, head_y, 20, 20)) #serves the purpose of house/starting point
    pygame.display.update()
    clock.tick(fps)
 
 
pygame.quit()
