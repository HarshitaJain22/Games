import pygame
pygame.init()

window = pygame.display.set_mode((660,660))
pygame.display.set_caption("Connect Four!")

red = (255,0,0)
yellow = (255,255,0)

global board
board = [[2,2,2,2,2,2,2],
         [2,2,2,2,2,2,2],
         [2,2,2,2,2,2,2],
         [2,2,2,2,2,2,2],
         [2,2,2,2,2,2,2],
         [2,2,2,2,2,2,2]]

            
def draw_circles():
    window.fill((100,200,255))
    x = 60
    y = 150
    for j in range(0,7):
        for i in range(0,6):
            pygame.draw.circle(window, (0,0,0), (x, y), 30)
            y += 90
        y = 150
        x += 90
    pygame.draw.line(window, (0,0,0), (0,90),(660,90),4)


def check_n_place(coinx,player_num):
    coin_y = 60
    col = coinx//94
    for i in range(1,7):
        if board[-i][col] == 2:
            board[-i][col] = player_num
            if i == 1: return 600
            elif i == 2: return 510
            elif i == 3: return 420
            elif i == 4: return 330
            elif i == 5: return 240
            elif i == 6: return 150
        else: pass

coins = []
coin_x = 60
coin_y = 60

def check_winner():
    pass

player = 0
color = red

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if coin_x < 600:
                    coin_x += 90
            elif event.key == pygame.K_LEFT:
                if coin_x > 60:
                    coin_x -= 90
            elif (event.key == pygame.K_SPACE) and (board[0][coin_x//94]==2):
                coin_y = check_n_place(coin_x, player)
                coins.append((coin_x, coin_y, color))
                coin_x = 60
                coin_y = 60
                if (player == 0) and (color == red):
                    player = 1
                    color = yellow
                elif (player == 1) and (color == yellow):
                    player = 0
                    color = red

    draw_circles()
    for i in range(0, len(coins)):
        pygame.draw.circle(window, coins[i][2],(coins[i][0],coins[i][1]),30)
    if player == 0:
        pygame.draw.circle(window, red,(coin_x,coin_y),30)
    else:
        pygame.draw.circle(window, yellow,(coin_x,coin_y),30)
    
    
    pygame.display.update()

pygame.quit()
