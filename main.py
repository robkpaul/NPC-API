from fastapi import FastAPI
import json, random

app = FastAPI()

class NPC:
    name = ''
    race = ''
    stats = {'str': 10, 'dex': 10, 'con': 10, 'int': 10, 'wis': 10, 'cha': 10}

    def toDict(self):
        as_dict = {}
        as_dict['name'] = self.name
        as_dict['race'] = self.race
        as_dict['stats'] = {'str': self.stats['str'], 
                            'dex': self.stats['dex'], 
                            'con': self.stats['con'], 
                            'int': self.stats['int'], 
                            'wis': self.stats['wis'], 
                            'cha': self.stats['cha'],
                            }
        return as_dict

names = open('./resources/names.json')
names = json.load(names)

@app.get('/')
def index():
    return 'active'

@app.get('/new')
def newNPC():
    npc = NPC()
    rand_race = random.randint(1,10)
    if rand_race == 1:
        npc.race = 'Dwarf'
    elif rand_race == 2:
        npc.race = 'Elf'
    elif rand_race == 3:
        npc.race = 'Halfling'
    elif rand_race == 4:
        npc.race = 'Dragonborn'
    elif rand_race == 5:
        npc.race = 'Gnome'
    elif rand_race == 6:
        npc.race = 'Tiefling'
    elif rand_race > 6: # ~40% chance of human
        npc.race = 'Human'

    npc.name = names[npc.race+'_first'][random.randint(0,len(names[npc.race+'_first'])-1)]
    if(npc.race != 'Elf' and npc.race != 'Tiefling'): # chooses last name of NPC, elves and tieflings have no last names, so ignores them.
        npc.name = npc.name + ' ' + names[npc.race+'_last'][random.randint(0,len(names[npc.race+'_last'])-1)]

    for stat in npc.stats: # randomizing stats: maximum 12, minimum 8 (assuming commoner stats for npcs)
        npc.stats[stat] = npc.stats[stat]-random.randint(-2,2)

    return npc.toDict()