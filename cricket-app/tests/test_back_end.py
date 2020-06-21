import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Players, Score
from os import getenv

class TestBase(TestCase):

    def create_app(self):

    
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()



class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


class TestPlayer(TestBase):

    def test_add_new_player(self):
        with self.client:
            response = self.client.post(
                '/player',
                data=dict(
                    first_name="Test f name",
                    last_name="Test l name",
                    email="fname.lastname@name.com"
                ),
                follow_redirects=True
            )
            self.assertIn(b'Test f name', response.data)



class TestScore(TestBase):
    def test_add_new_Score(self):
        with self.client:
            response = self.client.post(
                '/score',
                data=dict(
                    batting_runs=20,
                    wickets=3,
                    match_id=4,
                
                ),
                follow_redirects=True
            )
            self.assertIn(b'20', response.data)

class TestUpdate(TestBase):
    def test_update(self):
        with self.clint:
            response = self.clint.post(
                    '/update',
                    data=dict(
                        first_name="new f name",
                        last_name="new l name",
                        email="new@email.com"
                        ),
                    follow_redirects=True
             self.assertIn(b'20', response.data)
