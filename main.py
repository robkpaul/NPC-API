from fastapi import FastAPI
import json, random

app = FastAPI()

class NPC:
    name = ""
    race = ""

    


names = open("./resources/names.json")
names = json.load(names)

@app.get('/')
def index():
    return {'key' : 'value'}

@app.get('/new')
def newNPC():
    npc = NPC()
    randRace = random.randint(1,10)
    if randRace == 1:
        npc.race = "Dwarf"
    elif randRace == 2:
        npc.race = "Elf"
    elif randRace == 3:
        npc.race = "Halfling"
    elif randRace == 4:
        npc.race = "Dragonborn"
    elif randRace == 5:
        npc.race = "Gnome"
    elif randRace == 6:
        npc.race = "Tiefling"
    elif randRace > 6:
        npc.race = "Human"
    
    npc.name = names[npc.race+"_first"][random.randint(0,len(names[npc.race+"_first"])-1)]
    if(npc.race != "Elf" and npc.race != "Tiefling"):
        npc.name = npc.name + " " + names[npc.race+"_last"][random.randint(0,len(names[npc.race+"_last"])-1)]

    return npc