from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from application.models import Players


class PlayerForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    email = StringField('Email',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    content = StringField('Content',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    submit = SubmitField('Post Content')

class ScoreForm(FlaskForm):
    batting_runs = StringField('batting_runs',
            validators = [
                DataRequired()
            ]
    )
    wickets = StringField('wickets',
            validators = [
                DataRequired(),
                Length(min=0, max=30)
            ]
    )
    match_id = StringField('match_id',
            validators = [
                DataRequired(),
                Length(min=0, max=100)
            ]
    )
    Player_id = StringField('Player_id',
            validators = [
                DataRequired(),
                Length(min=0, max=100)
            ]
    )
    submit = SubmitField('Post Content')
