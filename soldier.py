import consts
def get_index_matrix(index):
    matrix=[]
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            matrix.append([index[0]+row,index[1]+col])
    return matrix


def is_in_grid(soldier_index):
    index_matrix = get_index_matrix(soldier_index)
    for row in range(len(index_matrix)):
        for col in range(len(soldier_index)[row]):
            if row >= consts.BOARD_ROWS or col >= consts.BOARD_COLS:
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
