from flask import Response, render_template, redirect, url_for, request
import random
from application import app

@app.route('/')

@app.route('/post/weapon', methods=['POST'])
def post_weapon():
    data_sent = request.data.decode('utf-8')
    if data_sent == 'Warrior':
        weapon = 'Axe'
    elif data_sent == 'Hunter':
        weapon = 'Bow'
    elif data_sent == 'Mage':
        weapon = 'Staff'
    elif data_sent == 'Pyro':
        weapon = 'Flame'
    elif data_sent == 'Knight':
        weapon = 'Sword'
        
    return Response(weapon, mimetype='text/plain')

