from time_logic import Game_time
from save import logo
import time
from datetime import datetime, timedelta
from numerize import numerize



second=1
minute=second*60
hour=60*minute
character_stat_list = {
    "Mjolnir":{
        "tick":5*second,
        "price":10
    },
    "Gungir":{
        "tick":minute,
        "price":100
    },
    "Draugnir":{
        "tick":5*minute,
        "price":1000
    },
    "Hringhorni":{
        "tick":30*minute,
        "price":50000
    },
    "Skidbladnir":{
        "tick":3*hour,
        "price":500000
    },
    "Gullinborsti":{
        "tick":5*hour,
        "price":5000000
    },
    "Brisingamen":{
        "tick":10*hour,
        "price":100000000
    },
    "Yggdrasil":{
        "tick":24*hour,
        "price":1000000000
    }
}

#seconds to hh:mm:ss

character_array = {}

def load_characters_from_save(save):
    for character_entity in save["characters"]:
        character = save["characters"][character_entity]
        name = character["name"]
        character_class_entity = Character(  name, 
                                            character['qty'], 
                                            character_stat_list[name]['tick'],
                                            character_stat_list[name]['price'])
        character_array[name] = character_class_entity
        print(character_class_entity)

class Character():
    def __init__(self, name, qty, tick, price):
        self.name = name
        self.qty = qty
        self.tick = tick
        self.price = price
    def __str__(self):
        return f"{self.name} \n    qty:{self.qty} \n    act time: {timedelta(seconds=self.tick)} \n    price: {numerize(self.price)}\n"





""" if __name__ == '__main__':
    d = timedelta(seconds=5)
    #print(d) """