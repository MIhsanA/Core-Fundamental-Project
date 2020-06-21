from application import app, db, bcrypt
from flask import Flask, render_template, redirect, url_for, request
from application.forms import PlayerForm, ScoreForm, UpdatePlayerForm
from application.models import Players, Score


@app.route('/')
@app.route('/home')
def home():
    scoreData = Score.query.all()
    playerData = Players.query.all()
    return render_template('home.html', title='Home', score=scoreData, players=playerData)

@app.route('/score', methods=['GET', 'POST'])
def score():
    form = ScoreForm()
    if form.validate_on_submit():
        scoreData = Score(
                batting_runs=form.batting_runs.data,
		wickets=form.wickets.data,
		match_id=form.match_id.data,
                player_id=form.player_id.data
                )
        db.session.add(scoreData)
        db.session.commit()
        return redirect(url_for('home'))

    else:
    	print(form.errors)
    return render_template('score.html', title='Score', form=form)

@app.route('/player', methods=['GET', 'POST'])
def player():
    form = PlayerForm()
    if form.validate_on_submit():
        playerData = Players(
                first_name=form.first_name.data,
	    	last_name=form.last_name.data,
    		email=form.email.data
                )
        db.session.add(playerData)
        db.session.commit()
        return redirect(url_for('home'))

    else:
    	print(form.errors)
    return render_template('player.html', title='Player', form=form)
@app.route('/player/delete/<int:cur_id>', methods=['GET', 'POST'])
def player_delete(cur_id):
    player = Players.query.filter_by(id=cur_id).first()
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:cur_id>', methods=['GET', 'POST'])
def player_update(cur_id):
    player = Players.query.filter_by(id=cur_id).first()
    form = UpdatePlayerForm()
    if form.validate_on_submit():
        player.first_name = form.first_name.data
        player.last_name = form.last_name.data
        player.email = form.email.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.first_name.data = player.first_name
        form.last_name.data = playerlast_name
        form.email.data = player.email
    return render_template('update.html', title='update',player=player, form=form)
