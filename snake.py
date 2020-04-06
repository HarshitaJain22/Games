import pygame
import random

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake (hisssssssssssss)")

fruit_x = random.randint(0,500)
fruit_y = random.randint(0,500)


def generate_food(head_x, head_y, fruit_x, fruit_y):

    fcentre_x = (20*(fruit_x//20))+10
    fcentre_y = (20*(fruit_y//20))+10

    if (fcentre_x == head_x) or (fcentre_y == head_y):
        fruit_x = random.randint(0,500)
        fruit_y = random.randint(0,500)
        fcentre_x = 20*(fruit_x//20)
        fcentre_y = 20*(fruit_y//20)

    pygame.draw.circle(window, (255,0,0), (fcentre_x, fcentre_y), 10)
    fruit_coordinates = [fcentre_x, fcentre_y]
    return fruit_coordinates

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


def check_interaction(position,fruitx, fruity):
    check_x = position[0]//20
    check_y = position[1]//20
    food_x = fruitx-10
    food_y = fruity-10
    10
    if (check_x == 25) or (check_y == 25) or (check_x == 0) or (check_y == 0):
        print("You Lost")
        return False
    elif (check_x == food_x) and (check_y == food_y):
        generate_food(position[0], position[1], fruitx, fruity)
    else:
        return True


run = True
head_x = 60
head_y = 100
fps = 5
clock = pygame.time.Clock()
velocity_x = 0
velocity_y = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            #pygame.quit()

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
    fruit_info = generate_food(head_x, head_y, fruit_x, fruit_y)
    head_x += velocity_x
    head_y += velocity_y
    head_pos = [head_x, head_y]
    run = check_interaction(head_pos, fruit_info[0], fruit_info[1])
    pygame.draw.rect(window, (0, 255,0) , (head_x, head_y, 20, 20))
    clock.tick(fps)
    pygame.display.update()


pygame.quit()
