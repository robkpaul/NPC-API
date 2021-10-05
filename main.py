from fastapi import FastAPI

app = FastAPI()

db = []

@app.get('/')
def index():
    return {'key' : 'value'}

@app.get('/npc')
def index():
    return {'name' : 'bob'}