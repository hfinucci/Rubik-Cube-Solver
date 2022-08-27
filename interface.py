import pygame
import sys
import cube
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
        case 0:  # BLUE
            return 0, 0, 255
        case 1:  # RED
            return 255, 0, 0
        case 2:  # GREEN
            return 60, 179, 113
        case 3:  # YELLOW
            return 255, 255, 100
        case 4:  # WHITE
            return 255, 255, 255
        case 5:  # ORANGE
            return 255, 165, 0
        case _:  # DEFAULT RETURNS BLACK
            return 0, 0, 0


def _draw_cube(x, y, cell_width, cell_height, colors):
    pygame.draw.rect(screen, calculate_color(colors[0]), (x, y, cell_width, cell_height), width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[1]), (MARGIN + x + cell_width, y, cell_width, cell_height),
                     width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[2]), (2 * MARGIN + x + cell_width * 2, y, cell_width, cell_height),
                     width=RECT_WIDTH)

    pygame.draw.rect(screen, calculate_color(colors[3]), (x, MARGIN + y + CELL_HEIGHT, 20, 20), width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[4]),
                     (MARGIN + x + cell_width, MARGIN + y + CELL_HEIGHT, cell_width, cell_height), width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[5]),
                     (2 * MARGIN + x + cell_width * 2, MARGIN + y + CELL_HEIGHT, cell_width, cell_height),
                     width=RECT_WIDTH)

    pygame.draw.rect(screen, calculate_color(colors[6]), (x, 2 * MARGIN + y + CELL_HEIGHT * 2, cell_width, cell_height),
                     width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[7]),
                     (MARGIN + x + cell_width, 2 * MARGIN + y + CELL_HEIGHT * 2, cell_width, cell_height),
                     width=RECT_WIDTH)
    pygame.draw.rect(screen, calculate_color(colors[8]),
                     (2 * MARGIN + x + cell_width * 2, 2 * MARGIN + y + CELL_HEIGHT * 2, cell_width, cell_height),
                     width=RECT_WIDTH)


def draw_cube(my_cube):
    _draw_cube(INITIAL_X + CUBE_WIDTH, INITIAL_Y, CELL_WIDTH, CELL_HEIGHT, my_cube[3].flatten())
    _draw_cube(INITIAL_X + CUBE_WIDTH, INITIAL_Y + CUBE_HEIGHT, CELL_WIDTH, CELL_HEIGHT, my_cube[4].flatten())
    _draw_cube(INITIAL_X + CUBE_WIDTH, INITIAL_Y + CUBE_HEIGHT * 2, CELL_WIDTH, CELL_HEIGHT, my_cube[1].flatten())
    _draw_cube(INITIAL_X, INITIAL_Y + CUBE_HEIGHT, CELL_WIDTH, CELL_HEIGHT, my_cube[0].flatten())
    _draw_cube(INITIAL_X + CUBE_WIDTH * 2, INITIAL_Y + CUBE_HEIGHT, CELL_WIDTH, CELL_HEIGHT, my_cube[2].flatten())
    _draw_cube(INITIAL_X + CUBE_WIDTH * 3, INITIAL_Y + CUBE_HEIGHT, CELL_WIDTH, CELL_HEIGHT, my_cube[5].flatten())


screen = pygame.display.set_mode(size)

# crear cubo
current_cube = cube.init_cube(3)

# las variables del cubo
print(cube.n_col)
print(cube.init_hash)

# hash del cubo
current_hash = cube.get_current_state(current_cube)
print(cube.is_done(current_hash))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    current_cube = cube.mix_up(current_cube, 1)
    draw_cube(current_cube)

    pygame.time.wait(200)
    pygame.display.flip()

