import Game_field
import consts
import Game_field
import pygame
import Screen
import soldier


state = {
    "soldier_index":[0,0],
    #The soldier's left corner
    "is_window_open": True,
    "state":consts.RUNNING_STATE

}

def main():
    pygame.init()
    Game_field.create_grid()

    while state["is_window_open"]:

        handle_user_events()
        if is_lose(state["soldier_index"]):
            state["state"]=consts.LOSE_STATE



def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if soldier.is_in_grid([state["soldier_index"][0],state["soldier_index"][1]+1]):
                    state["soldier_index"][1]+=1
            elif event.key == pygame.K_s:
                if soldier.is_in_grid([state["soldier_index"][0], state["soldier_index"][1] -1]):
                    state["soldier_index"][1]-=1
            elif event.key == pygame.K_a:
                if soldier.is_in_grid([state["soldier_index"][0]-1, state["soldier_index"][1]]):
                    state["soldier_index"][0] -= 1
            elif event.key == pygame.K_d:
                if soldier.is_in_grid([state["soldier_index"][0]+1, state["soldier_index"][1]]):
                    state["soldier_index"][0] += 1
            elif event.key==pygame.K_KP_ENTER:
        #מראים את המסך עם הרשת
                pass



def is_lose(soldier_index):
    index_list=soldier.get_feet(soldier_index)
    for index in index_list:
        if index in Game_field.find_flag_indexes():
            return True
    return False

def is_win(soldier_index):
   index_list=soldier.get_feet(soldier_index)
   for index in index_list:
       if index in Game_field.find_mines_indexes():
           return True
   return False

