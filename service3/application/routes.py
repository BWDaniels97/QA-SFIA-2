from flask import Response, render_template, redirect, url_for, request
import random
from application import app

@app.route('/')

@app.route('/get/race', methods=['GET'])
def get_race():

    race = ['Goblin', 'Elf', 'Human', 'Dwarf', 'Ork']
    chosen = random.choice(race)
    return Response(chosen, mimetype='text/plain')