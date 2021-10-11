from fastapi import FastAPI
import json, random

app = FastAPI()

class NPC:
    name = ''
    anc = ''
    stats = {'str': 10, 'dex': 10, 'con': 10, 'int': 10, 'wis': 10, 'cha': 10}

    def toDict(self):
        as_dict = {}
        as_dict['name'] = self.name
        as_dict['ancestry'] = self.anc
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
    rand_anc = random.randint(1,10)
    if rand_anc == 1:
        npc.anc = 'Dwarf'
    elif rand_anc == 2:
        npc.anc = 'Elf'
    elif rand_anc == 3:
        npc.anc = 'Halfling'
    elif rand_anc == 4:
        npc.anc = 'Dragonborn'
    elif rand_anc == 5:
        npc.anc = 'Gnome'
    elif rand_anc == 6:
        npc.anc = 'Tiefling'
    elif rand_anc > 6: # ~40% chance of human
        npc.anc = 'Human'

    npc.name = names[npc.anc+'_first'][random.randint(0,len(names[npc.anc+'_first'])-1)]
    if(npc.anc != 'Elf' and npc.anc != 'Tiefling'): # chooses last name of NPC, elves and tieflings have no last names, so ignores them.
        npc.name = npc.name + ' ' + names[npc.anc+'_last'][random.randint(0,len(names[npc.anc+'_last'])-1)]

    for stat in npc.stats: # randomizing stats: maximum 12, minimum 8 (assuming commoner stats for npcs)
        npc.stats[stat] = npc.stats[stat]-random.randint(-2,2)

    return npc.toDict()

@app.get('/new/{anc}')
def newNPC(anc: str):
    npc = NPC()
    npc.anc = anc
    
    npc.name = names[npc.anc+'_first'][random.randint(0,len(names[npc.anc+'_first'])-1)]
    if(npc.anc != 'Elf' and npc.anc != 'Tiefling'): # chooses last name of NPC, elves and tieflings have no last names, so ignores them.
        npc.name = npc.name + ' ' + names[npc.anc+'_last'][random.randint(0,len(names[npc.anc+'_last'])-1)]

    for stat in npc.stats: # randomizing stats: maximum 12, minimum 8 (assuming commoner stats for npcs)
        npc.stats[stat] = npc.stats[stat]-random.randint(-2,2)

    return npc.toDict()