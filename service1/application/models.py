from application import db

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_class = db.Column(db.String(50), nullable=False)
    character_race = db.Column(db.String(50), nullable=False)
    character_weapon = db.Column(db.String(50), nullable=False)

    