from application.models import Posts
from flask import render_template
from application import app, db
from application.forms import PostForm

@app.route('/')
@app.route('/home')
def home():

    form = PostForm()
    opts = []
    hero = Posts.query.all()
    for name in hero:
        opts.append(name.character_name)

    form.heroclass.choices = opts

    hero = Posts.query.filter_by(character_name=form.heroclass.data).first()

    return render_template('home.html', title='Home', form=form)


    
    
    