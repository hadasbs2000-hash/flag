from flag import consts
import pygame
import random
import solider

field_grid=[]

def create_empty_grid():
    global field_grid
    for i in range(consts.BOARD_ROWS):
        field_grid.append([])
        for j in range(consts.BOARD_COLS):
            field_grid.append([])
def put_flag():
    pass


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
            field_grid[rnd_row].insert(rnd_col,)#mine!!!! and do it 3 times)
            #then make these cells occupied(??) or it already checks it

def find_flag_indexes():
    pass
def find_mines_indexes():
    pass
def create_grid():
    pass

