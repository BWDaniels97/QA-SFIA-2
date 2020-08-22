from flask import Response, render_template, redirect, url_for, request
import random
from application import app

@app.route('/')

@app.route('/get/class', methods=['GET'])
def get_class():

    heroClass = ['Warrior', 'Hunter', 'Mage', 'Knight', 'Pyro']
    chosen = random.choice(heroClass)
    return Response(chosen, mimetype='text/plain')