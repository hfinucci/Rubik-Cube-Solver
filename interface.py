import sys, pygame
from cube import Cube
from constants import *

pygame.init()

size = width, height = 700, 540

MARGIN = 2
INITIAL_X = 20
INITIAL_Y = 20
RECT_WIDTH = 0
CELL_WIDTH = 20
CELL_HEIGHT = 20
CUBE_WIDTH = 3 * CELL_WIDTH + 3 * MARGIN 
CUBE_HEIGHT = 3 * CELL_HEIGHT + 3 * MARGIN

BLACK_RGB = 0, 0, 0
BACKGROUND_COLOR = (225, 225, 225)


def calculate_color(number):
    match number:
        case 0: # BLUE
            return (0,0,255)
        case 1: # RED
            return (255,0,0)
        case 2: # GREEN
            return (60,179,113)
        case 3: # YELLOW
            return (255,255,100)
        case 4: # WHITE
            return (255,255,255)
        case 5: # ORANGE
            return (255,165,0)
        case _: # DEFAULT RETURNS BLACK
            return (0,0,0)


def draw_cube(x, y, cell_width, cell_height, colors):
    pygame.draw.rect(screen, calculate_color(colors[0]), (x,y,cell_width,cell_height), width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[1]), (MARGIN+x+cell_width,y,cell_width,cell_height), width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[2]), (2*MARGIN+x+cell_width*2,y,cell_width,cell_height), width=RECT_WIDTH)

    pygame.draw.rect(screen, calculate_color(colors[3]), (x,MARGIN+y+CELL_HEIGHT,20,20), width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[4]), (MARGIN+x+cell_width,MARGIN+y+CELL_HEIGHT,cell_width,cell_height), width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[5]), (2*MARGIN+x+cell_width*2,MARGIN+y+CELL_HEIGHT,cell_width,cell_height), width=RECT_WIDTH)

    pygame.draw.rect(screen, calculate_color(colors[6]), (x,2*MARGIN+y+CELL_HEIGHT*2,cell_width,cell_height), width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[7]), (MARGIN+x+cell_width,2*MARGIN+y+CELL_HEIGHT*2,cell_width,cell_height), width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[8]), (2*MARGIN+x+cell_width*2,2*MARGIN+y+CELL_HEIGHT*2,cell_width,cell_height), width=RECT_WIDTH)


screen = pygame.display.set_mode(size)

cube = Cube(3)

# cube.RotateXAxis(0,RIGHT)
# cube.RotateXAxis(2,LEFT)
ticks = 2000
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(BACKGROUND_COLOR)

    draw_cube(INITIAL_X + CUBE_WIDTH, INITIAL_Y, CELL_WIDTH, CELL_HEIGHT, cube.cube[2].flatten())
    draw_cube(INITIAL_X + CUBE_WIDTH, INITIAL_Y + CUBE_HEIGHT, CELL_WIDTH, CELL_HEIGHT, cube.cube[5].flatten())
    draw_cube(INITIAL_X + CUBE_WIDTH, INITIAL_Y + CUBE_HEIGHT * 2, CELL_WIDTH, CELL_HEIGHT, cube.cube[0].flatten())
    draw_cube(INITIAL_X, INITIAL_Y + CUBE_HEIGHT, CELL_WIDTH, CELL_HEIGHT, cube.cube[3].flatten())
    draw_cube(INITIAL_X + CUBE_WIDTH * 2, INITIAL_Y + CUBE_HEIGHT, CELL_WIDTH, CELL_HEIGHT, cube.cube[1].flatten())
    draw_cube(INITIAL_X + CUBE_WIDTH * 3, INITIAL_Y + CUBE_HEIGHT, CELL_WIDTH, CELL_HEIGHT, cube.cube[4].flatten())

    pygame.time.wait(100)
    cube.RotateXAxis(0,RIGHT)
    pygame.time.wait(100)
    cube.RotateYAxis(2,UP)
    pygame.time.wait(100)
    cube.RotateXAxis(2,LEFT)
    pygame.time.wait(100)
    cube.RotateYAxis(1,DOWN)
    pygame.time.wait(100)
    cube.RotateZAxis(3,CLOCKWISE)
    pygame.time.wait(100)
    cube.RotateYAxis(0,DOWN)

    pygame.display.flip()




