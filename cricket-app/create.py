from application import db
from application.models import Players, Score


db.drop_all()
db.create_all()

