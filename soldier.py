import pygame.image
import consts
soldier_img = pygame.transform.scale(pygame.image.load("bin/soldier.png"),
                                         ( consts.SOLDIER_ROWS * consts.CELL_SIZE, consts.SOLDIER_COLS * consts.CELL_SIZE))
import consts

def get_index_matrix(index):
    matrix=[]
    for row in range(consts.SOLDIER_ROWS):
        for col in range(consts.SOLDIER_COLS):
            matrix.append([index[0]+row,index[1]+col])
    return matrix


def is_in_grid(soldier_index):
    index_matrix = get_index_matrix(soldier_index)
    """for inex in range(len(index_matrix)):
        for col in range(len(index_matrix)[row]):"""
    if index_matrix[-1][0]>= consts.BOARD_ROWS or index_matrix[-1][1]>= consts.BOARD_COLS:
        return False
    return True


def get_feet(index):
    feet_index=[]
    for r in range(consts.SOLDIER_FEET_ROWS):
        for c in range(consts.SOLDIER_COLS):
            feet_index.append([index[0] + consts.SOLDIER_BODY_ROWS +r, index[1] + c])
    return feet_index


def get_body(index):
    body_index=[]
    for r in range(consts.SOLDIER_BODY_ROWS):
        for c in range(consts.SOLDIER_COLS):
            body_index.append([index[0] + r, index[1] + c])
    return body_index

