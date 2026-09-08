import consts
import pygame
import math
import Game_field


screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)

def draw_border():
    line_y = (consts.NUM_OF_LINES_LOSE - 1) * consts.BUBBLE_RADIUS * 2 - (
        consts.NUM_OF_LINES_LOSE - 2) * consts.ROWS_OVERLAP
    pygame.draw.line(screen, consts.BORDER_COLOR, start_pos=(0, line_y),
                     end_pos=(consts.WINDOW_WIDTH, line_y))
def draw_mine():
    pass
def draw_soilder():

# grid_node_width = 10
# grid_node_height = 10 #???is pixels?steps?
#
# def createSquare(x, y, color):
#     pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height ])
#
#
#
# def visualizeGrid():
#     y = 0  # we start at the top of the screen
#     for row in Game_field.field_grid:
#         x = 0 # for every row we start at the left of the screen again
#         for item in row:
#             if item == 0:
#                 createSquare(x, y, (255, 255, 255))
#             else:
#                 createSquare(x, y, (0, 0, 0))
#
#             x += grid_node_width # for ever item/number in that row we move one "step" to the right
#         y += grid_node_height   # for every new row we move one "step" downwards
#     pygame.display.update()
#
#
#   # call the function
# while True:
#     pass  # keeps the window open so you can see the result.
#
