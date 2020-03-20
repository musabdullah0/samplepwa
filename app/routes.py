from flask import Flask, render_template, url_for, request, redirect
from app import app
import pyrebase
from app.mapper import map
import sys

config = {
    "apiKey": "AIzaSyAjD_4z3oC3J0LedswgDmTXILI2dWzDcQ4",
    "authDomain": "moose-sample-pwa.firebaseapp.com",
    "databaseURL": "https://moose-sample-pwa.firebaseio.com",
    "projectId": "moose-sample-pwa",
    "storageBucket": "moose-sample-pwa.appspot.com",
    "messagingSenderId": "960867862502",
    "appId": "1:960867862502:web:26d749e76cf7946b833827",
    "measurementId": "G-NSZWYWHJZD"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    print('This is standard output', file=sys.stdout)
    if (request.method == 'POST'):
        email = request.form['name']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            #user_id = auth.get_account_info(user['idToken'])
            #session['usr'] = user_id
            return redirect(url_for('home'))
        except:
            unsuccessful = 'Please check your credentials'
            return render_template('index.html', umessage=unsuccessful)
    return render_template('index.html')


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if (request.method == 'POST'):
        email = request.form['name']
        password = request.form['password']
        auth.create_user_with_email_and_password(email, password)
        return render_template('index.html')
    return render_template('create_account.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', map=map)


# putting the relative route in manifest.json wouldn't work, so jank it is
@app.route('/icon')
def icon():
    return app.send_static_file('img/icon-256x256.png')


# another jank way of stuffing the service worker away
@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')
