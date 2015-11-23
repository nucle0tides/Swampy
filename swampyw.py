import json 
import urllib2 

class Shrek(object): 
    def __init__(self): 
        self.json_file = json.load(urllib2.urlopen('http://gabbyortman.me/shrek/shrek_new.json'))

    def get_all_characters(self): 
        return self.json_file['Shrek']['All Characters']

    def get_all_scenes(self): 
        return self.json_file['Shrek']['All Scenes']

    def get_scene_action(self, scene): 
        if scene.upper() in self.json_file['Shrek']['All Scenes']: 
            return self.json_file['Shrek']['Scene Actions'][scene.upper()]
        else: 
            raise ValueError("That scene is not in the cinematic classic, Shrek!")

    def get_character_lines(self, character): 
        if character.upper() in self.json_file['Shrek']['All Characters']: 
            return self.json_file['Shrek']['Character Lines'][character.upper()]
        else: 
            raise ValueError("That character is not in the cinematic classic, Shrek!")