from application import db

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(50), nullable=False)

    