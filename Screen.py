import pygame
import random
import consts
import Game_field


BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20  # pixels per cell
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE
GRASS_COUNT = 20
FLAG_ROWS = 3
FLAG_COLS = 4
FLAG_INDEX = [BOARD_ROWS - FLAG_ROWS, BOARD_COLS - FLAG_COLS]
MINES_COUNT = 20
MINE_ROWS = 1
MINE_COLS = 3
SOLDIER_ROWS = 4
SOLDIER_COLS = 2

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def drow_soldier(soldiers_index):
    soldier_img = pygame.transform.scale(pygame.image.load(r"C:\Users\jbt\PycharmProjects\flag\bin\soldier.png"),
                                         (FLAG_COLS * CELL_SIZE, FLAG_ROWS * CELL_SIZE))
    soldier_y = soldiers_index[0] * CELL_SIZE
    soldier_x = soldiers_index[1] * CELL_SIZE
    rect = soldier_img.get_rect(topleft=(soldier_x, soldier_y))
    screen.blit(soldier_img, rect)


def drow_night_soldier(soldiers_index):
    soldier_img = pygame.transform.scale(pygame.image.load(r"C:\Users\jbt\PycharmProjects\flag\bin\soldier_night.png"),
                                         (FLAG_COLS * CELL_SIZE, FLAG_ROWS * CELL_SIZE))
    soldier_y = soldiers_index[0] * CELL_SIZE
    soldier_x = soldiers_index[1] * CELL_SIZE
    rect = soldier_img.get_rect(topleft=(soldier_x, soldier_y))
    screen.blit(soldier_img, rect)


#מיקומים רנדומלים לשיחים
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


#מתודה לציור רנדומלי של שיחים
def blit_grass(grass_list, grass_img):
    for rect in grass_list:
        screen.blit(grass_img, rect)


def drow_flag():
    imp = pygame.image.load(r"C:\Users\jbt\PycharmProjects\flag\bin\flag.png")
    flag_img = pygame.transform.scale(imp, (FLAG_COLS * CELL_SIZE, FLAG_ROWS * CELL_SIZE))
    flag_y = FLAG_INDEX[0] * CELL_SIZE
    flag_x = FLAG_INDEX[1] * CELL_SIZE
    rect = flag_img.get_rect(topleft=(flag_x, flag_y))
    screen.blit(flag_img, rect)



def run_screen():
    # Fill the background color to the screen
    screen.fill(consts.GREEN)
    # pygame.init()
    grass_img = pygame.transform.scale(pygame.image.load(r"C:\Users\jbt\PycharmProjects\flag\bin\grass.png"), (50, 30))
    # לעשות את הערכים בקבועים
    blit_grass(grass_location(grass_img), pygame.image.load(r"C:\Users\jbt\PycharmProjects\flag\bin\grass.png"))
    drow_flag()
    #drow_soldier(screen,[0,0])
    # return screen


#drow_soldier(run_screen(),[0,0])
# pygame.display.flip()


def dark_screen_background():
    # screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    background_colour = 'black'
    screen.fill(background_colour)
    for i in range(BOARD_ROWS * CELL_SIZE):
        for j in range(BOARD_COLS * CELL_SIZE):
            pygame.draw.line(screen, consts.GREEN, (i * CELL_SIZE, 0), (i * CELL_SIZE, BOARD_ROWS * CELL_SIZE), 1)
        for j in range(BOARD_COLS * CELL_SIZE):
            pygame.draw.line(screen, consts.GREEN, (0, j * CELL_SIZE), (BOARD_COLS * CELL_SIZE, j * CELL_SIZE), 1)
    # return screen


def drow_mines(mine_index_list):
    imp = pygame.image.load(r"C:\Users\jbt\PycharmProjects\flag\bin\mine.png")
    mine_img = pygame.transform.scale(imp, (MINE_COLS * CELL_SIZE, MINE_ROWS * CELL_SIZE))
    for index in mine_index_list:
        mine_x = index[0] * CELL_SIZE
        mine_y = index[1] * CELL_SIZE
        rect = mine_img.get_rect(topleft=(mine_x, mine_y))
        screen.blit(mine_img, rect)


def run_dark_screen():
    # screen=dark_screen_background()
    dark_screen_background()
    # index_list = [[0, 0], [5, 5], [7, 7], [10, 10], [20, 20]]#change!!!!
    # drow_mines(index_list)
    drow_soldier([0, 0])
    pygame.display.flip()

run_dark_screen()
# Variable to keep our game loop running
running = True


# game loop
while running:


   # for loop through the event queue
   for event in pygame.event.get():


       # Check for QUIT event
       if event.type == pygame.QUIT:
           running = False
#vvbdb