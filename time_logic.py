import time
import datetime
import math
import os 
from save import logo

class Game_time():
    current_time=0
    def __init__(self, save):
        self.start_game = save['time-start']
    
    def get_time(self):
        self.current_time = math.ceil(time.time()-self.start_game)
        return self.current_time





if __name__ == '__main__':
    os.system("cls")
    logo()
    save = {'time-start': 1637007307}
    game = Game_time(save)
    
    for x in range(1,10):
        time.sleep(1)
        print(game.get_time())