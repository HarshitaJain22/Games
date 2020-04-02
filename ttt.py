import pygame as pg
pg.init()

window = pg.display.set_mode((550,550))
pg.display.set_caption("Tic-Tac-Toe")

class Block:
    def __init__(self, color, position, status):
        self.color = color
        self.position = position
        self.status = status

    def draw_block(self):
        pg.draw.rect(window, self.color, self.position)

    def area_of_block(self):
        dim = self.position
        x = [int(dim[0]), int(dim[0])+int(dim[2])]
        y = [int(dim[1]), int(dim[1])+int(dim[3])]
        range_pos = [x[0], x[1] ,y[0], y[1]]
        return range_pos        
        
first = Block((255,255,255),(25,25,150,150),True)
second = Block((255,255,255),(200,25,150,150),True)
third = Block((255,255,255),(375,25,150,150),True)
fourth = Block((255,255,255),(25,200,150,150),True)
fifth = Block((255,255,255),(200,200,150,150),True)
sixth = Block((255,255,255),(375,200,150,150),True)
seventh = Block((255,255,255),(25,375,150,150),True)
eighth = Block((255,255,255),(200,375,150,150),True)
ninth = Block((255,255,255),(375,375,150,150),True)

blocks = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]

def make_blocks(blocks):
    window.fill((0,0,0))
    for i in range (9):
        blocks[i].draw_block()
        blocks[i].status = True

def intersection(blocks):
    ranges = []
    for i in range (9):
        ranges.append(blocks[i].area_of_block())
    return ranges

def play_again(blocks, font):
    play_again_yes = pg.draw.rect(window, (0, 0, 255), (125,300,300,125))
    play_again_text = font.render("Play Again?", True, (255,255,255))   
    window.blit(play_again_text,( 125+((300-play_again_text.get_width())//2), 300+((125-play_again_text.get_height())//2)))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.MOUSEBUTTONUP:
            position = pg.mouse.get_pos()
            if play_again_yes.collidepoint(position):
                pg.display.update()
                make_blocks(blocks)
                game(True, blocks, font)


def x_wins(blocks, font):
    pg.draw.rect(window, (255, 0, 255), (125,125,300,125))
    x_text = font.render("X Wins!", True, (0,0,0))   
    window.blit(x_text,( 125+((300-x_text.get_width())//2), 125+((125-x_text.get_height())//2)))
    play_again(blocks, font)

def o_wins(blocks, font):
    pg.draw.rect(window, (0, 255, 0), (125,125,300,125))
    o_text = font.render("O Wins!", True, (0,0,0))   
    window.blit(o_text,( 125+((300-o_text.get_width())//2), 125+((125-o_text.get_height())//2)))
    play_again(blocks, font)

run = True
font = pg.font.SysFont("comicsansms", 35)
def game(running, blocks, font):
    run = running
    x_in = [ ]
    o_in = [ ]
    player = 1
    make_blocks(blocks)
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    player = 1
                    x_in.clear()
                    o_in.clear()
                    make_blocks(blocks)
                    
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                ranges = intersection(blocks)
                if (pos[0] in range (ranges[0][0],ranges[0][1]) and (pos[1] in range (ranges[0][2], ranges[0][3]))) and first.status:
                    if player == 1:
                        pg.draw.line(window, (255,0,255), (50,50),(150,150), 4)
                        pg.draw.line(window, (255,0,255), (150,50),(50,150), 4)
                        x_in.append(1)
                        player = 2
                    else:
                        pg.draw.circle(window, (0,255,0), (100,100),50)
                        pg.draw.circle(window, (255,255,255), (100,100),46)
                        o_in.append(1)
                        player = 1
                    first.status = False
                if (pos[0] in range (ranges[1][0],ranges[1][1]) and (pos[1] in range (ranges[1][2], ranges[1][3]))) and second.status:
                    if player == 1:
                        pg.draw.line(window, (255,0,255), (225,50),(325,150), 4)
                        pg.draw.line(window, (255,0,255), (225,150),(325,50), 4)
                        x_in.append(2)
                        player = 2
                    else:
                        pg.draw.circle(window, (0,255,0), (275,100),50)
                        pg.draw.circle(window, (255,255,255), (275,100),46)
                        o_in.append(2)
                        player = 1
                    second.status = False
                if (pos[0] in range (ranges[2][0],ranges[2][1]) and (pos[1] in range (ranges[2][2], ranges[2][3]))) and third.status:
                    if player == 1:
                        pg.draw.line(window, (255,0,255), (400,50),(500,150), 4)
                        pg.draw.line(window, (255,0,255), (400,150),(500,50), 4)
                        x_in.append(3)
                        player = 2
                    else:
                        pg.draw.circle(window, (0,255,0), (450,100),50)
                        pg.draw.circle(window, (255,255,255), (450,100),46)
                        o_in.append(3)
                        player = 1
                    third.status = False
                if (pos[0] in range (ranges[3][0],ranges[3][1]) and (pos[1] in range (ranges[3][2], ranges[3][3]))) and fourth.status:
                    if player == 1:
                        pg.draw.line(window, (255,0,255), (50,225),(150,325), 4)
                        pg.draw.line(window, (255,0,255), (150,225),(50,325), 4)
                        x_in.append(4)
                        player = 2
                    else:
                        pg.draw.circle(window, (0,255,0), (100,275),50)
                        pg.draw.circle(window, (255,255,255), (100,275),46)
                        o_in.append(4)
                        player = 1
                    fourth.status = False
                if (pos[0] in range (ranges[4][0],ranges[4][1]) and (pos[1] in range (ranges[4][2], ranges[4][3]))) and fifth.status:
                    if player == 1:
                        pg.draw.line(window, (255,0,255), (225,225),(325,325), 4)
                        pg.draw.line(window, (255,0,255), (325,225),(225,325), 4)
                        x_in.append(5)
                        player = 2
                    else:
                        pg.draw.circle(window, (0,255,0), (275,275),50)
                        pg.draw.circle(window, (255,255,255), (275,275),46)
                        o_in.append(5)
                        player = 1
                    fifth.status = False
                if (pos[0] in range (ranges[5][0],ranges[5][1]) and (pos[1] in range (ranges[5][2], ranges[5][3]))) and sixth.status:
                    if player == 1:
                        pg.draw.line(window, (255,0,255), (400,225),(500,325), 4)
                        pg.draw.line(window, (255,0,255), (500,225),(400,325), 4)
                        x_in.append(6)
                        player = 2
                    else:
                        pg.draw.circle(window, (0,255,0), (450,275),50)
                        pg.draw.circle(window, (255,255,255), (450,275),46)
                        o_in.append(6)
                        player = 1
                    sixth.status = False
                if (pos[0] in range (ranges[6][0],ranges[6][1]) and (pos[1] in range (ranges[6][2], ranges[6][3]))) and seventh.status:
                    if player == 1:
                        pg.draw.line(window, (255,0,255), (50,400),(150,500), 4)
                        pg.draw.line(window, (255,0,255), (150,400),(50,500), 4)
                        x_in.append(7)
                        player = 2
                    else:
                        pg.draw.circle(window, (0,255,0), (100,450),50)
                        pg.draw.circle(window, (255,255,255), (100,450),46)
                        o_in.append(7)
                        player = 1
                    seventh.status = False
                if (pos[0] in range (ranges[7][0],ranges[7][1]) and (pos[1] in range (ranges[7][2], ranges[7][3]))) and eighth.status:
                    if player == 1:
                        pg.draw.line(window, (255,0,255), (225,400),(325,500), 4)
                        pg.draw.line(window, (255,0,255), (325,400),(225,500), 4)
                        x_in.append(8)
                        player = 2
                    else:
                        pg.draw.circle(window, (0,255,0), (275,450),50)
                        pg.draw.circle(window, (255,255,255), (275,450),46)
                        o_in.append(8)
                        player = 1
                    eighth.status = False
                if (pos[0] in range (ranges[8][0],ranges[8][1]) and (pos[1] in range (ranges[8][2], ranges[8][3]))) and ninth.status:
                    if player == 1:
                        pg.draw.line(window, (255,0,255), (400,400),(500,500), 4)
                        pg.draw.line(window, (255,0,255), (500,400),(400,500), 4)
                        x_in.append(9)
                        player = 2
                    else:
                        pg.draw.circle(window, (0,255,0), (450,450),50)
                        pg.draw.circle(window, (255,255,255), (450,450),46)
                        o_in.append(9)
                        player = 1
                    ninth.status = False

        x_in.sort()
        o_in.sort()
        score_at = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for i in range (0,8):
            if (score_at[i][0] in x_in) and (score_at[i][1] in x_in) and (score_at[i][2] in x_in):
                o_in.clear()
                make_blocks(blocks)
                x_wins(blocks, font)
            elif (score_at[i][0] in o_in) and (score_at[i][1] in o_in) and (score_at[i][2] in o_in):
                x_in.clear()
                make_blocks(blocks)
                o_wins(blocks, font)
        
        pg.display.update()
        
    pg.quit()
    quit()

game(run, blocks, font)
