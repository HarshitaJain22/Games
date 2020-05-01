import pygame 

pygame.init() 
 
window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("PONG!") 
  
paddle_ax = 20
paddle_ay = 250
paddle_bx = 760
paddle_by = 250

puck_x = 400
puck_y = 300

puck_speed = 20
vel_x = 20
vel_y = 20

width = 20
height = 100

vel = 30

fps = 5
clock = pygame.time.Clock()

run = True

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_UP] and paddle_by > 0:
        paddle_by -= vel

    if keys[pygame.K_DOWN] and paddle_by < 500:
        paddle_by += vel

    if keys[pygame.K_w] and paddle_ay > 0:
        paddle_ay -= vel

    if keys[pygame.K_s] and paddle_ay < 500:
        paddle_ay += vel
   
    if (puck_y > 575) or ((puck_y - 10) < 10): #575 and 10 is majboori
        vel_y *= -1

    if (puck_x > 780) or (puck_x < 20):
        puck_x = 400
        puck_y = 300

    if (puck_x+10 in range(paddle_bx, paddle_bx+width)) and (puck_y in range(paddle_by , paddle_by+height)):
        vel_x *= -1

    if (puck_x-10 in range(paddle_ax, paddle_ax+width)) and (puck_y in range(paddle_ay , paddle_ay+height)):
        vel_x *= -1
        
    puck_x += vel_x
    puck_y += vel_y
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (paddle_ax, paddle_ay, width, height))
    pygame.draw.rect(window, (255, 0, 0), (paddle_bx, paddle_by, width, height))
    pygame.draw.circle(window, (255, 255, 255), (puck_x, puck_y),10)

    pygame.display.update()
    clock.tick(fps)

pygame.quit() 
