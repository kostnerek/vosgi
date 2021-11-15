import json
import os
from template_save import template_save

def logo():
    print("""
                         .__ 
___  ______  ______ ____ |__|
\  \/ /  _ \/  ___// ___\|  |
 \   (  <_> )___ \/ /_/  >  |
  \_/ \____/____  >___  /|__|
                \/_____/
            
            """)

def get_saves():
    if not os.listdir("./save"):
        return None
    return os.listdir("./save")

def get_save_name(save_file_name):
    with open(f"save/{save_file_name}", encoding='utf8') as outfile:
        save = json.load(outfile)
        return save['save-name']

def choose_save():
    if not os.listdir("./save"):
        print("No saves, please create one!")
        return create_save()
    else:
        c=0
        print("Choose save:")
        saves = get_saves()
        for save_file_name in saves:
            print(f"[{c}]: ",get_save_name(save_file_name))
            c+=1
        print("Or create new one![n]")
        
        user_save_choose_input = input("What you want to do?: ")
        try:
            index = int(user_save_choose_input)
            try:
                return load_save(saves[index])
            except:
                os.system("cls")
                print("Not correct value!")
                logo()
                return choose_save()
        except:
            return create_save()

def create_save():
    
    saves = get_saves()
    if not saves:
        save_file_name = "save1"
        save_num=1
    else:
        a = saves[-1]
        save_num = int(a[a.find("e")+1:a.find(".")])+1
    save_name = input("Insert your save name: ")
    template_save['save-name'] = save_name
    with open(f"save/save{save_num}.json", 'w', encoding='utf8') as outfile:
        json.dump(template_save, outfile, ensure_ascii=False)
    return load_save(f"save{save_num}.json")

def load_save(save_file_name):
    save_name = get_save_name(save_file_name)
    print(f"Loading save '{save_name}'")
    with open(f"save/{save_file_name}", encoding='utf8') as outfile:
        save = json.load(outfile)
        return save


def load_game():
    os.system("cls")
    logo()
    return choose_save()

