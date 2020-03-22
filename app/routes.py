from flask import Flask, render_template, url_for, request, redirect, jsonify, flash
from flask_dance.contrib.google import make_google_blueprint, google
from app import app
from app.mapper import map
from secrets import config

import pyrebase

firebase = pyrebase.initialize_app(config)
db = firebase.database()

blueprint = make_google_blueprint(
    client_id='1061850404553-a06a91h7a8moiogjjhm8fsb7evkj9h17.apps.googleusercontent.com',
    client_secret="SVIcwOuR1gIN2JVGC0XvVtzz",
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")


@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    try:
        resp = google.get("/oauth2/v3/userinfo")
    except:
        return redirect(url_for("google.login"))
    email = resp.json()['email']
    name = resp.json()['name']
    update_users(email, name)

    flash('ready to work, ' + name + '?', 'success')
    return render_template('home.html', map=map, user=resp.json())


def update_users(email, name):
    users = [u.val() for u in db.child("users").get().each()]
    emails = [u['email'] for u in users]

    if email not in emails:
        account = {'name': name, 'email': email}
        db.child('users').push(account)
        print('pushed new account', account)


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', map=map)

# send config values to all templates
@app.context_processor
def inject_test():
    return {'pyconfig': config}

# putting the relative route in manifest.json wouldn't work, so jank it is
@app.route('/icon')
def icon():
    return app.send_static_file('img/icon-256x256.png')


# another jank way of stuffing the service worker away
@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')
