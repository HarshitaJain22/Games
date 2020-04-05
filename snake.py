import pygame as pg
import random

window = pg.display.set_mode((500,500))
pg.display.set_caption("Snake (hisssssssssssssssssss)")

#def make_grid():
rows = 25
run = True
def draw_head():
    head_x = random.randint(0,500)
    head_y = random.randint(0,500)
    pg.draw.rect(window, (255,0,0), (20*(head_x//20), 20*(head_y//20),25,25))


while run:
    window.fill((255,255,255))
    diff = 20
    x = 0
    y = 0
    for i in range (0,25):
        x = x + diff
        y = y + diff
        pg.draw.line(window, (0,0,0), (x,0), (x,500))
        pg.draw.line(window, (0,0,0), (0,y), (500,y))        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    draw_head()
    pg.display.update()

pg.quit()
