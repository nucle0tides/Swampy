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

    def get_nth_line(self, character, line): 
        if character.upper() in self.json_file['Shrek']['All Characters'] and len(self.json_file['Shrek']['Character Lines'][character.upper()]) > line: 
            return self.json_file['Shrek']['Character Lines'][character.upper()][line]
        else: 
            raise ValueError("This is bad error handling. Either the character you've picked isn't in the cinematic classic, Shrek or they don't have that many lines")
    
    def how_many_times_one_character(self, character, word): 
        count = 0 
        current_character = self.get_character_lines(character.upper())
        for i in range(len(current_character)): 
            if word.lower() in current_character[i].lower(): 
                count += 1
        return count

    def how_many_times_all_characters(self, word): 
        count = 0
        character_set = self.json_file['Shrek']['Character Lines']
        #TODO not have this be n^3...jesus Gabby
        for val in character_set: 
            for sentence in character_set[val]: 
                if word.lower() in sentence.lower(): 
                    count += 1
        return count

shrek = Shrek() 
print shrek.get_nth_line("Shrek", 50)