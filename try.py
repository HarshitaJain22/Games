import pygame
pygame.init()

window = pygame.display.set_mode((660,660))
pygame.display.set_caption("Connect Four!")

red = (255,0,0)
yellow = (255,255,0)

global board
board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]

            
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


def check_n_place(coinx, player_num):
    coin_y = 60
    col = coinx//94
    for i in range(1,7):
        if board[-i][col] == 0:
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
    for i in range(0,6):
        for j in range(0,4):
            if (board[i][j] == board[i][j+1]) and (board[i][j+1] == board[i][j+2]) and (board[i][j+2] == board[i][j+3]):
                player_num = board[i][j]
                if player_num == 0:
                    pass
                else:
                    print("Player" + str(player_num) + "wins!")
                    break
            if (j!=3) and (board[j][i] == board[j+1][i]) and (board[j+1][i] == board[j+2][i]) and (board[j+2][i] == board[j+3][i]):
                player_num = board[j][i]
                if player_num == 0:
                    pass
                else:
                    print("Player" + str(player_num) + "wins!")
                    break
            if (i<3) and (board[i][j] == board[i+1][j+1]) and (board[i+1][j+1] == board[i+2][j+2]) and (board[i+2][j+2] == board[i+3][j+3]):
                player_num = board[j][i]
                if player_num == 0:
                    pass
                else:
                    print("Player" + str(player_num) + "wins!")
                    break

player = 1
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
            elif (event.key == pygame.K_SPACE) and (board[0][coin_x//94]==0):
                coin_y = check_n_place(coin_x, player)
                coins.append((coin_x, coin_y, color))
                coin_x = 60
                coin_y = 60
                if (player == 1) and (color == red):
                    player = 2
                    color = yellow
                elif (player == 2) and (color == yellow):
                    player = 1
                    color = red

    draw_circles()
    for i in range(0, len(coins)):
        pygame.draw.circle(window, coins[i][2],(coins[i][0],coins[i][1]),30)
    if player == 1:
        pygame.draw.circle(window, red,(coin_x,coin_y),30)
    else:
        pygame.draw.circle(window, yellow,(coin_x,coin_y),30)
    
    check_winner()
    pygame.display.update()

pygame.quit()
