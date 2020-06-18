from application import app, db, bcrypt
from flask import render_template, url_for
from application.forms import PlayerForm, ScoreForm
from application.models import Players, Score


@app.route('/')
@app.route('/home')
def home():
    scoreData = Score.query.all()
    playerData = Players.query.all()
    return render_trmplate('home.html', title='Home', score=scoreData, players=playerData)

@app.route('/score', methods=['GET', 'POST'])
def score():
	form = ScoreForm()
	if form.validate_on_submit():
		scoreData = Score(
			batting_run=form.batting_run.data,
			wickets=form.wickets.data,
			match_id=form.match_id.data,

		)
		db.session.add(scoreData)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		print(form.errors)
	return render_template('score.html', title='Score', form=form)

