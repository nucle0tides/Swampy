import json
shrek = 'shrek.txt'

#character dialog len(line) - len(line.lstrip()) == 25 
#other len(line) - len(line.lstrip()) == 15 
#scene len(line) - len(line.lstrip()) == 15 && line.strip().isupper()
#character name len(line) - len(line.lstrip()) == 37
        
def get_shreked(filename): 
    shrek = open(filename, 'r')
    shrek_dict = dict()
    current_character = ""
    for line in shrek: 
        if len(line) - len(line.lstrip()) == 37: 
            current_character = line.strip()
        if current_character not in shrek_dict: 
            shrek_dict[current_character] = []
    shrek.seek(0)
    character_line = ""
    #could I have done this in one go? probably. is it worth it? nah. 
    for line in shrek:
        if len(line) - len(line.lstrip()) == 37: 
            current_character = line.strip()
        elif len(line) - len(line.lstrip()) == 25: 
            character_line += line.strip() + " "
        elif len(character_line) != 0: 
            shrek_dict[current_character].append(character_line.strip())
            character_line = ""
    shrek.close()
    return shrek_dict

#DUPLICATE CODE, I /KNOW/ AND I DONT CARE RIGHT NOW
def get_shreked_scenes(filename):
    shrek = open(filename, 'r')
    scene_dict = dict() 
    curr_scene = ""
    curr_action = ""
    for line in shrek: 
        if len(line) - len(line.lstrip()) == 15 and line.isupper(): 
            curr_scene = line.strip() 
        if curr_scene not in scene_dict: 
            scene_dict[curr_scene] = []
    shrek.seek(0)
    for line in shrek: 
        if len(line) - len(line.lstrip()) == 15 and line.isupper(): 
            curr_scene = line.strip() 
        elif (len(line) - len(line.lstrip()) == 15) and not line.isupper(): 
            curr_action += line.strip() + " "
        elif len(curr_action) != 0:
            if "Allstar" in curr_action: 
                scene_dict["Allstar"] = ["" + curr_action]
                curr_action = ""
            else: 
                scene_dict[curr_scene].append(curr_action.strip())
                curr_action = ""
    shrek.close()
    return scene_dict

def shrek_characters(filename): 
    shrek = open(filename, 'r')
    shrek_chars = list()
    current_character = ""
    for line in shrek: 
        if len(line) - len(line.lstrip()) == 37: 
            current_character = line.strip()
        if current_character not in shrek_chars: 
            shrek_chars.append(current_character)
    shrek.close()
    return shrek_chars

def shrek_scenes(filename): 
    shrek = open(filename, 'r')
    scene_list = list() 
    curr_scene = ""
    for line in shrek: 
        if len(line) - len(line.lstrip()) == 15 and line.isupper(): 
            curr_scene = line.strip() 
        if curr_scene not in scene_list: 
            scene_list.append(curr_scene)
    shrek.close()
    return scene_list

character_list = shrek_characters(shrek)
scene_list = shrek_scenes(shrek)
character_lines = get_shreked(shrek)
scene_actions = get_shreked_scenes(shrek)
shrek_dict = { "Shrek" : {"All Characters" : character_list, "All Scenes" : scene_list, "Character Lines" : character_lines, "Scene Actions" : scene_actions} }
json = json.dumps(shrek_dict)
shrek_json = open('shrek_new.json', 'w')
shrek_json.write(json)