from application.models import Posts
from flask import render_template
from application import app, db
from application.forms import PostForm
from sqlalchemy import func

@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')


@app.route('/generate')
def generate():

    return render_template('generate.html', title='Generate')

    

@app.route('/generate/hero')
def generatehero():
    heroClass = Posts.query.filter_by(character_name.data).order_by(func.random()).first()
    city = requests.get('http://35.197.235.71:5001/get/city')
    race = requests.get('http://35.197.235.71:5002/get/race')
    
    weapon = requests.post('http://35.197.235.71:5003/post/weapon', data=heroClass.text)
    
    return render_template('generate.html', title='Generate', weapon=weapon.text, city=city.text, race=race.text, heroClass=heroClass.text)