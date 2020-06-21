import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Players, Score 

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app


    def setUp(self):
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/muhammad_786_ihsan/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestPlayer(TestBase): 
    def test_player(self):

        self.driver.find_element_by_xpath('/html/body/div/a[3]').click()
        time.sleep(5)
        
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys('Ihsan') 
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys('Almas')
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('Ihsan@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click() 
        time.sleep(5) 
        assert url_for('home') in self.driver.current_url









if __name__ == '__main__':
    unittest.main(port=5000)
