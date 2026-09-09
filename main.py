import time

import Game_field
import consts
import Game_field
import pygame
import Screen
import soldier
from flag.flag.Screen import drow_soldier, run_screen

state = {
    "soldier_index":[0,0],
    #The soldier's left corner
    "is_window_open": True,
    "state":consts.RUNNING_STATE

}

def main():
    pygame.init()
    Game_field.create_grid()
    Screen.run_screen()

    while state["is_window_open"]:

        handle_user_events()
        if is_lose(state["soldier_index"]):
            state["state"]=consts.LOSE_STATE



def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        soldier_y = state["soldier_index"][0] * consts.CELL_SIZE
        soldier_x = state["soldier_index"][1] * consts.CELL_SIZE
        this_rect = soldier.soldier_img.get_rect(topleft=(soldier_x, soldier_y))
        keys=pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:

            if keys[pygame.K_RIGHT]:
                if soldier.is_in_grid([state["soldier_index"][0], state["soldier_index"][1] + 1]):
                    state["soldier_index"][1] += 1

            elif keys[pygame.K_LEFT]:
                if soldier.is_in_grid([state["soldier_index"][0], state["soldier_index"][1] - 1]):
                    state["soldier_index"][1] -= 1

            elif keys[pygame.K_DOWN]:
                if soldier.is_in_grid([state["soldier_index"][0] - 1, state["soldier_index"][1]]):
                    state["soldier_index"][0] -= 1

            elif keys[pygame.K_UP]:
                if soldier.is_in_grid([state["soldier_index"][0] + 1, state["soldier_index"][1]]):
                    state["soldier_index"][0] += 1

            elif event.key == pygame.K_KP_ENTER:
                Screen.run_dark_screen(state["soldier_index"])
                time.sleep(1)
                Screen.run_screen()

            # Screen.move_soldier(this_rect, state["soldier_index"])
            pygame.Rect.move(this_rect,state["soldier_index"][0] * consts.CELL_SIZE,state["soldier_index"][1] * consts.CELL_SIZE)

            if is_lose(state["soldier_index"]):
                state["state"]=consts.LOSE_STATE
            if is_win(state["soldier_index"]):
                state["state"] = consts.WIN_STATE


def is_lose(soldier_index):
    index_list = soldier.get_feet(soldier_index)
    for index in index_list:
        if Game_field.field_grid[index[0]][index[1]]==consts.MINE:
            return True
    return False


def is_win(soldier_index):

   index_list = soldier.get_feet(soldier_index)
   for index in index_list:
       if index in Game_field.find_flag_indexes():
           return True
   return False
main()