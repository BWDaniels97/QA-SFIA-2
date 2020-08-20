from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Posts


class PostForm(FlaskForm):
    
    heroclass = SelectField("Hero Class", choices=[], validators = [])

    hero_name = StringField("Hero Name",
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )

