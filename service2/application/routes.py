from flask import Response, render_template, redirect, url_for, request
import random
from application import app

@app.route('/')

@app.route('/get/city', methods=['GET'])
def get_city():

    city = ['Olishull', 'Yharnam', 'Lothric', 'Bruma', 'Kvatch']
    chosen = random.choice(city)
    return Response(chosen, mimetype='text/plain')