import pygame
import random
from consts import *
import Game_field
import soldier
from flag.flag.soldier import soldier_img

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def drow_soldier(soldiers_index):
    soldier_y = soldiers_index[0] * CELL_SIZE
    soldier_x = soldiers_index[1] * CELL_SIZE
    rect = soldier.soldier_img.get_rect(topleft=(soldier_x, soldier_y))
    screen.blit(soldier.soldier_img, rect)


def drow_night_soldier(soldiers_index):
    soldier_img = pygame.transform.scale(pygame.image.load("bin/soldier_night.png"),
                                         (FLAG_COLS * CELL_SIZE, FLAG_ROWS * CELL_SIZE))
    soldier_y = soldiers_index[0] * CELL_SIZE
    soldier_x = soldiers_index[1] * CELL_SIZE
    rect = soldier_img.get_rect(topleft=(soldier_x, soldier_y))
    screen.blit(soldier_img, rect)



def grass_location(grass_img):
    grass_rect_list = []
    while len(grass_rect_list) < GRASS_COUNT:

        grass_x = random.randrange(50, WINDOW_WIDTH - 50)
        grass_y = random.randrange(30, WINDOW_HEIGHT - 30)
        rect = grass_img.get_rect(
            topleft=(grass_x, grass_y))
        if rect not in grass_rect_list:
            grass_rect_list.append(rect)
    return grass_rect_list


def blit_grass(grass_list, grass_img):
    for rect in grass_list:
        screen.blit(grass_img, rect)


def drow_flag():
    imp = pygame.image.load("bin/flag.png")
    flag_img = pygame.transform.scale(imp, (FLAG_COLS * CELL_SIZE, FLAG_ROWS * CELL_SIZE))
    flag_y = FLAG_INDEX[0] * CELL_SIZE
    flag_x = FLAG_INDEX[1] * CELL_SIZE
    rect = flag_img.get_rect(topleft=(flag_x, flag_y))
    screen.blit(flag_img, rect)



def run_screen():
    # Fill the background color to the screen
    screen.fill(GREEN)
    # pygame.init()
    grass_img = pygame.transform.scale(pygame.image.load("bin/grass.png"), (50, 30))
    blit_grass(grass_location(grass_img), grass_img)
    drow_flag()
    drow_soldier([0,0])
    pygame.display.flip()
    # return screen


#drow_soldier(run_screen(),[0,0])
# pygame.display.flip()


def dark_screen_background():
   # pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    background_colour = 'black'
    screen.fill(background_colour)
    for i in range(BOARD_ROWS * CELL_SIZE):
        for j in range(BOARD_COLS * CELL_SIZE):
            pygame.draw.line(screen, GREEN, (i * CELL_SIZE, 0), (i * CELL_SIZE, BOARD_ROWS * CELL_SIZE), 2)
        for j in range(BOARD_COLS * CELL_SIZE):
            pygame.draw.line(screen, GREEN, (0, j * CELL_SIZE), (BOARD_COLS * CELL_SIZE, j * CELL_SIZE), 2)
    # return screen


def drow_mines(mine_index_list):
    print(mine_index_list)
    imp = pygame.image.load("bin/mine.png")
    mine_img = pygame.transform.scale(imp, (MINE_COLS * CELL_SIZE, MINE_ROWS * CELL_SIZE))
    for index in mine_index_list:
        mine_x = index[1]* CELL_SIZE
        mine_y = index[0] * CELL_SIZE
        rect = mine_img.get_rect(topleft=(mine_x, mine_y))
        screen.blit(mine_img, rect)


def run_dark_screen(soldier_index):
    dark_screen_background()
    index_list = Game_field.mine_list#change!!!!
    drow_mines(index_list)
    drow_night_soldier(soldier_index)
    drow_flag()
    pygame.display.flip()

def move_soldier(this_rect,soldier_index):
    soldier_x= soldier_index[0] * CELL_SIZE
    soldier_y=soldier_index[1] * CELL_SIZE
    rect=soldier_img.get_rect(topleft=(soldier_x,soldier_y))
    screen.blit(screen,rect)
"""def is_pressed_enter():
    if keyboard.read_key() == key.:
run_screen()
# Variable to keep our game loop running
running = True


print("press enter")
var = getkey()

if var == keys.ENTER:
  print("You pressed enter")"""
"""run_dark_screen()
running = True
# game loop
while running:


   # for loop through the event queue
   for event in pygame.event.get():


       # Check for QUIT event
       if event.type == pygame.QUIT:
           running = False
#vvbdb"""