import pygame
import random

pygame.init()

# 10 x 20, 25 each box => 250 x 500, min
win_wid = 650
win_h = 540
play_wid = 250
play_h = 500
block_size = 25

top_left_x = (win_wid - play_wid) // 2
top_left_y = win_h - play_h

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
 
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
      def __init__(self, x, y, shape):
            self.x = x
            self.y = y
            self.shape = shape
            self.color = shape_colors[shapes.index(shape)]
            self.rotation = 0

      
def create_grid(locked_pos = {}):
      grid = [[(0,0,0) for x in range(10)]for x in range(20)]
      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  if (j,i) in locked_pos:
                        c = locked_pos[(j,i)]
                        grid[i][j] = c
      return grid

def convert_shape(shape_data):
      positions = []
      formatting = shape_data.shape[shape_data.rotation % len(shape_data.shape) ]
      
      for i, line in enumerate(formatting):
            row = list(line)
            for j, column in enumerate(row):
                  if column == "0":
                        positions.append((shape_data.x + j , shape_data.y + i))

      for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)
            #positions[i] = (pos[0], pos[1])

      return positions

def valid_space(shape, grid):
      accepted_pos = [[(j,i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
      accepted_pos = [j for sub in accepted_pos for j in sub]
      
      formatted = convert_shape(shape)

      for pos in formatted:
            if pos not in accepted_pos:
                  if pos[1] > -1:
                        return False
      return True


def check_lost(positions):
      for pos in positions:
            x, y = pos
            if y < 1:
                  return True

      return False

def get_shape():
      return Piece(5, 0, random.choice(shapes))

def draw_text_mid():
      pass

def draw_grid(window, grid):
      sx = top_left_x
      sy = top_left_y

      for i in range(20):
            pygame.draw.line(window, (120, 120,120), (sx, sy + (i*block_size)), (sx + play_wid, sy + (i*block_size)))
            for j in range(10):
                  pygame.draw.line(window, (120, 120,120), (sx + (j*block_size), sy), (sx + (j*block_size), sy + play_h))

        
def clear_rows(grid, locked):

      inc = 0
      for i in range(len(grid)-1,-1,-1):
            row = grid[i]
            if (0,0,0) not in row:
                  inc += 1
                  ind = i
                  for j in range(len(row)):
                        try:
                              del locked[(j,i)]
                        except:
                              continue
      
      if inc > 0:
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                  x, y = key
                  if y < ind:
                        newKey = (x, y + inc)
                        locked[newKey] = locked.pop(key)
      

      

def draw_next_shape(shape_data, window):
      font = pygame.font.SysFont('comicsans', 30)
      label = font.render('Next Shape:', 1, (255,255,255))
      
      sx = top_left_x + play_wid + 50 # check if this works for you
      sy = top_left_y + play_h/2 -50
      format_it = shape_data.shape[shape_data.rotation % len(shape_data.shape) ]

      for i, line in enumerate(format_it):
            row = list(line)
            for j, column in enumerate(row):
                  if column == "0":
                        pygame.draw.rect(window, shape_data.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)

      window.blit(label, (sx+10, sy-30))


def draw_window(window, grid):
      window.fill((0,0,0))

      font = pygame.font.SysFont("comicsans", 25)

      label = font.render("TETRIS", 1, (255,255,255))

      window.blit(label, ((top_left_x + (play_wid/2) - (label.get_width()/2)), 20))

      for i in range(20):
            for j in range(10):
                  pygame.draw.rect(window, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

      pygame.draw.rect(window, (255, 0, 0), (top_left_x, top_left_y, play_wid, play_h), 4)

      draw_grid(window, grid)
      


def main(window):

      locked_positions = {}
      grid = create_grid(locked_positions)

      change_piece = False
      run = True
      current_piece = get_shape()
      next_piece = get_shape()
      clock = pygame.time.Clock()
      fall_time = 0
      score = 0
      
      while run:
            fall_speed = 0.25

            grid = create_grid(locked_positions)
            fall_time += clock.get_rawtime()
            clock.tick()

            if fall_time/1000 > fall_speed:
                  fall_time = 0
                  current_piece.y += 1
                  if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                        current_piece.y -= 1
                        change_piece = True
                        
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        run = False
                        pygame.display.quit()
            
                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                              current_piece.x -= 1
                              if not valid_space(current_piece, grid):
                                    current_piece.x += 1
            
                        elif event.key == pygame.K_RIGHT:
                              current_piece.x += 1
                              if not valid_space(current_piece, grid):
                                    current_piece.x -= 1

                        elif event.key == pygame.K_UP:
                              # rotate shape
                              current_piece.rotation += 1
                              if not valid_space(current_piece, grid):
                                    current_piece.rotation -= 1
            
                        if event.key == pygame.K_DOWN:
                              # move shape down
                              current_piece.y += 1
                              if not valid_space(current_piece, grid):
                                    current_piece.y -= 1

            shape_pos = convert_shape(current_piece)

            for i in range(len(shape_pos)):
                  x, y = shape_pos[i]
                  if y > -1:
                        grid[y][x] = current_piece.color

            if change_piece:
                  for pos in shape_pos:
                        p = (pos[0], pos[1])
                        locked_positions[p] = current_piece.color
                  current_piece = next_piece
                  next_piece = get_shape()
                  change_piece = False

                  clear_rows(grid, locked_positions)

            draw_window(window, grid)
            draw_next_shape(next_piece, window)
            pygame.display.update()

            if check_lost(locked_positions):
                  run = False

      

 
def main_menu(window):
      main(window)



window = pygame.display.set_mode((win_wid,win_h))
pygame.display.set_caption("Tetris")
main_menu(window)
