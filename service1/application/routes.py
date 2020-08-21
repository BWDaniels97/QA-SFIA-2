from application.models import Posts
from application import app, db
from application.forms import PostForm
from sqlalchemy import func, desc
from flask import render_template, redirect, url_for, request
import requests

@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')


@app.route('/generate')
def generate():

    return render_template('generate.html', title='Generate')

    

@app.route('/generate/hero', methods=['GET', 'POST'])
def generatehero():
    
    heroClass = requests.get('http://35.197.235.71:5001/get/class')
    race = requests.get('http://35.197.235.71:5002/get/race')
    weapon = requests.post('http://35.197.235.71:5003/post/weapon', data=heroClass.text)

    herodata = Posts(
                character_class = heroClass.text,
                character_race = race.text,
                character_weapon = weapon.text)
    
    db.session.add(herodata)
    db.session.commit()

    chosen_hero = Posts.query.order_by(desc(Posts.id)).limit(1).all()

    
    return render_template('generate.html', title='Generate', chosen_hero=chosen_hero)


