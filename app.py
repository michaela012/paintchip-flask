from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import *


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'create account':
            return redirect(url_for('register'))
        if action == 'log in':
            return redirect(url_for('authenticate'))

    return render_template('index.html')


# TODO: handle account creation
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        # ensure uname and email are unique, else give error
        email_exists = db.session.query(db.exists().where(User.email == email)).scalar()
        user_exists = db.session.query(db.exists().where(User.username == user)).scalar()

        if email_exists or user_exists:
            if user_exists:
                error = "username in use, please try another"

        else:
            new_user = User(username=user,
                            email=email)
            new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        return render_template('register.html')


# TODO: handle authentification
@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'POST':
        print(request.form.get('username'))

    else:
        return render_template('authenticate.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pass
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)