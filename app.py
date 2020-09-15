from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        action = request.form.get('action')
        user = request.form.get('username')
        user_exists = db.session.query(db.exists().where(User.username == user)).scalar()

        # TODO: change returns to error flashing (give feedback on page)
        if action == 'check availability':
            if user_exists:
                pass;
                # return 'in use'
            else:
                return 'not in use'
        else:    # action == create account
            password = request.form.get('password')
            email = request.form.get('email')

            # ensure uname and email are unique, else give error
            email_exists = db.session.query(db.exists().where(User.email == email)).scalar()

            if email_exists or user_exists:
                if user_exists:
                    error = "username in use, please try another"
                else:
                    error = "email already associated with an existing account"
                return error

            else:
                new_user = User(username=user,
                                email=email)
                new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('home', username=user))

    else:   # request.method == 'GET'
        return render_template('register.html')


# TODO: handle authentification
@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'POST':
        user = request.form.get('username')
        print(request.form.get(user))
        return redirect(url_for('home', username=user))

    else:
        return render_template('authenticate.html')


@app.route('/home/<username>', methods=['GET', 'POST'])
@login_required
def home(username):
    if request.method == 'POST':
        pass
    else:
        return render_template('home.html', user=username)

if __name__ == '__main__':
    app.run(debug=True)