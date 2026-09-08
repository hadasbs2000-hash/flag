from flag import consts
import pygame
import random
import Screen

field_grid=[]
flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS

def create_empty_grid():
    global field_grid
    for i in range(consts.BOARD_ROWS):
        field_grid.append([])
        for j in range(consts.BOARD_COLS):
            field_grid.append([])

def random_mines_in_grid():
    rnd_row=random.randint(0,consts.BOARD_ROWS)
    rnd_col=random.randint(0,consts.BOARD_COLS-1)
    #so it won't be out of range
    count=0
    for i in range(consts.MINES_COUNT):
        for j in range(consts.MINE_COLS):
            if field_grid[rnd_row][j+rnd_col]=="":#if its empty
                count+=1
        if count==3:
            field_grid[rnd_row].insert(rnd_col,)#add the mine!!!! and do it 3 times)
            #then make these cells occupied(??) or it already checks it

def find_flag_indexes():
    flag_index=[]
    for row in range(consts.FLAG_ROWS,0,-1):
        for col in range(consts.FLAG_COLS,0,-1):
            flag_index.append([row,col])
    return flag_index

def draw():
    for row in field_grid:
        for cell in row:
            if image in cell:#אם יש תמונה כלומר את המוקש במיקום הזה אז לצייר אותו על המסך
                Screen.draw_mine()
                #גם דגל וחייל פה? ההדפסה?


def find_mines_indexes():
    pass
