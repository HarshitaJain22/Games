import pygame
import random
 
pygame.init()
 
window = pygame.display.set_mode((500,540))
pygame.display.set_caption("Snake (hisssssssssssss)")

global run 
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
 
font = pygame.font.SysFont("Bookman Old Style", 18)
global scores
scores = []
def display_score(font):
    score = len(scores)
    pygame.draw.rect(window, (255, 255,0) , (5, 5, 150,30))
    score_num = font.render(str(score), True, (0,0,0))
    score_text = font.render("SCORE:", True, (0,0,0))
    window.blit(score_text,( 5+((100-score_text.get_width())//2), 5+((30-score_text.get_height())//2)))
    window.blit(score_num,( 105, 5+((30-score_num.get_height())//2)))


font2 = pygame.font.SysFont("Bookman Old Style", 32)
def game_over(show_string):
    window.fill((0,0,0))
    game_over_text = font2.render("GAME OVER :(", True, (255,255,255))
    print_string = font2.render(show_string, True, (255,255,255))
    score_string = font2.render("Your Score was:", True, (255,255,255))
    score_num_string = font2.render(str(len(scores)), True, (255,255,255))
    window.blit(game_over_text,(((500-game_over_text.get_width())//2),180))
    window.blit(print_string,(((500-print_string.get_width())//2),240))
    window.blit(score_string,(((500-score_string.get_width())//2)-30,300))
    window.blit(score_num_string,(score_string.get_width()+((500-score_string.get_width())//2),300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

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
        #print("You Lost! GAME OVER")
        game_over("You hit a wall.")
        return False
        #pygame.quit()
    else:
        return True

 
def check_food(fruitx, fruity, sxores):
    food_x = fruitx-10
    food_y = fruity-10
    if (body_info[0][0] == food_x) and (body_info[0][1] == food_y):
        global fcentre_x #TIP: This is a horrible way to do this, but it works. You should instead have a function which returns these values and set it elsewhere
        global fcentre_y
        fcentre_x, fcentre_y = generate_food(body_info[0][0], body_info[0][1])
        scores.append(1)
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
    display_score(font)
    coordinates(velocity_x, velocity_y)
    draw_body()
    pygame.draw.circle(window, (255,0,0), (fcentre_x, fcentre_y), 10)
    run = check_collision()
    for i in range (1,len(body_info)):
        if body_info[0] == body_info[i]:
            game_over("You bit yourself.")
            run = False
            break
    check_food(fcentre_x, fcentre_y, scores)
    pygame.display.update()
    clock.tick(fps)
