from itertools import count

import consts
import pygame
import random
#import Screen
import soldier
from flag.flag.consts import MINE_ROWS, MINE_COLS
field_grid=[]
mine_list=[]
flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS

def create_empty_grid():
    global field_grid
    for i in range(consts.BOARD_ROWS):
        field_grid.append([])
        for j in range(consts.BOARD_COLS):
            field_grid[i].append(consts.EMPTY)


def put_in_flag():
    global field_grid
    for r in range(flag_row-1,consts.BOARD_ROWS):
        for c in range(flag_col-1,consts.BOARD_COLS):
            field_grid[r][c]="FLAG"



def check_random_mine(mine_index):
    this_mine_list = []
    for i in range(consts.MINE_ROWS):
        for j in range(consts.MINE_COLS):
            if mine_index[0] + i < consts.BOARD_ROWS and mine_index[1] + j < consts.BOARD_COLS:
                if field_grid[mine_index[0]+ i][mine_index[1] + j] == consts.EMPTY:    # if its empty
                    this_mine_list.append([mine_index[0]+ i,mine_index[1] + j])
    if len(this_mine_list)== MINE_ROWS * MINE_COLS:
        return this_mine_list
    else:
        return []
def crate_list(index):
   global mine_list
   mine_list.append(index)

def random_mines_in_grid():

    mines_count=0
    while mines_count<consts.MINES_COUNT:
        rnd_row=random.randint(0,consts.BOARD_ROWS-1)
        rnd_col=random.randint(0,consts.BOARD_COLS-1)
        if field_grid[rnd_row][rnd_col]==consts.EMPTY:
            if [rnd_row,rnd_col] not in soldier.get_index_matrix([0,0]):
                this_mine_list = check_random_mine([rnd_row,rnd_col])
                if len(this_mine_list)>0:
                        for index in  this_mine_list:
                           crate_list(index)
                           field_grid[index[0]][index[1]]=consts.MINE
                        mines_count+=1


"""    count=0
   
            field_grid[rnd_row][rnd_col].insert(rnd_col,)#add the mine!!!! and do it 3 times)
            #then make these cells occupied(??) or it already checks it"""

def find_flag_indexes():
    #רשימה של האינדקסים שהיא שם
    flag_index=[]
    for r in range(consts.FLAG_ROWS,0,-1):
        for c in range(consts.FLAG_COLS,0,-1):

            flag_index.append([r,c])
    return flag_index


def find_mines_indexes():
    pass

"""def draw():
    for row in field_grid:
        for cell in row:
            if image in cell:#אם יש תמונה כלומר את המוקש במיקום הזה אז לצייר אותו על המסך
                Screen.draw_mine()
                #גם דגל וחייל פה? ההדפסה?"""

def create_grid():
    create_empty_grid()
    put_in_flag()
    random_mines_in_grid()

create_grid()



def hi():
    create_grid()
    for row in range(len(field_grid)):
        for col in range (len(field_grid[row])):
             print(field_grid[row][col], end=' ')
        print()

hi()