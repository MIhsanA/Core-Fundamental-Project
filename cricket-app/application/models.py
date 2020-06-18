from application import db
from datetime import datetime

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batting_runs = db.Column(db.Integer, nullable=False, default=0)
    wickets = db.Column(db.Integer, nullable=False, default=0)
    match_id = db.Column(db.Integer, nullable=False)
    date_played = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'Player ID: ', self.player_id, '\r\n',
            'Score: ', self.batting_runs, '\r\n', self.wickets
        ])


class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), unique=True)
    score = db.relationship('Score', backref='play')

    def __repr__(self):
        return ''.join(['PlayerID: ', str(self.id), '\r\n',
        'Email: ', self.email], '\r\n',
        'Name: ', self.first_name, ' ', self.last_name
        )

