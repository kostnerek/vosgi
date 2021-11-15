from save import load_game,logo
from time_logic import Game_time
from characters import load_characters_from_save



import json
import os
def load_default_save():
    os.system('cls')
    logo()
    with open('save/save1.json', 'r') as f:
        save = json.load(f)
    return save

""" proper way of starting game """
#save = load_game()
save = load_default_save()

game_time = Game_time(save)
load_characters_from_save(save)

