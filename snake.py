import pygame
import random
 
pygame.init()
 
window = pygame.display.set_mode((500,540))
pygame.display.set_caption("Snake (hisssssssssssss)")
 
run = True
 
head_x = 100
head_y = 140

fps = 5
clock = pygame.time.Clock()
 
velocity_x = 0
velocity_y = 0

global body_info
body_info = []

head_pos = [head_x, head_y]
body_info.append(head_pos)

def generate_food(head_x, head_y):
    fruit_x = random.randint(0,499)
    fruit_y = random.randint(40,539)
    fcentre_x = (20*(fruit_x//20))+10
    fcentre_y = (20*(fruit_y//20))+10

    for i in range (0, len(body_info)):
        if (fcentre_x-10 == body_info[i][0]) and (fcentre_y-10 == body_info[i][1]):
            fruit_x = random.randint(0,499)
            fruit_y = random.randint(40,539)
            fcentre_x = 20*(fruit_x//20)+10
            fcentre_y = 20*(fruit_y//20)+10

    fruit_coordinates = (fcentre_x, fcentre_y)
    return fruit_coordinates

 
def make_grid():
    window.fill((255,255,255))
    diff = 20
    x = 0
    y = 20
    for i in range (0,25):
        x = x + diff
        y = y + diff
        pygame.draw.line(window, (0,0,0), (x,40), (x,540))
        pygame.draw.line(window, (0,0,0), (0,y), (500,y))
 
scores = []
def display_score(score):
    score.append(1)
    print(len(score))

def coordinates(velx, vely):
    for i in range (1,len(body_info)):
        body_info[-i][0] = body_info[-(i+1)][0]
        body_info[-i][1] = body_info[-(i+1)][1]
    
    body_info[0][0] += velx
    body_info[0][1] += vely


def increase_len():
    new_block_x = body_info[-1][0] - 20
    new_block_y = body_info[-1][1]
    add_thing = [new_block_x, new_block_y]
    body_info.append(add_thing)
    draw_body()


def draw_body():
    l = len(body_info)
    for i in range (0,l):
        pygame.draw.rect(window, (0, 255,0) , (body_info[i][0], body_info[i][1], 20,20))
        pygame.draw.circle(window, (100,100,100), (body_info[i][0]+10, body_info[i][1]+10), 3)
    pygame.draw.rect(window, (0, 0,0) , (body_info[0][0]+4, body_info[0][1]+4, 12, 12))
    
def check_collision():
    check_x = body_info[0][0]//20
    check_y = body_info[0][1]//20
    if (check_x > 25) or (check_y > 27) or (check_x < 0) or (check_y < 2):
        print("You Lost")
        #return False
        pygame.quit()
    else:
        return True

 
def check_food(fruitx, fruity, sxores):
    food_x = fruitx-10
    food_y = fruity-10
    if (body_info[0][0] == food_x) and (body_info[0][1] == food_y):
        global fcentre_x #TIP: This is a horrible way to do this, but it works. You should instead have a function which returns these values and set it elsewhere
        global fcentre_y
        fcentre_x, fcentre_y = generate_food(body_info[0][0], body_info[0][1])
        display_score(sxores)
        increase_len()

fcentre_x, fcentre_y = generate_food(head_x, head_y)

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
    coordinates(velocity_x, velocity_y)
    draw_body()
    pygame.draw.circle(window, (255,0,0), (fcentre_x, fcentre_y), 10)
    run = check_collision()
    for i in range (1,len(body_info)):
        if body_info[0] == body_info[i]:
            print("you ate yourself,lol")
            #run = False
            pygame.quit()
    check_food(fcentre_x, fcentre_y, scores)
    pygame.display.update()
    clock.tick(fps)
 
 
pygame.quit()
