import pygame as pg

window = pg.display.set_mode((500,500))
pg.display.set_caption("Snake (hisssssssssssssssssss)")

#def make_grid():
rows = 25
run = True
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
    pg.display.update()

pg.quit()
