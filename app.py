from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import requests
from sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = 'pasdan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define custom filter function
def jinja2_enumerate(iterable, start=0):
    return enumerate(iterable, start=start)

# Register the custom filter with Jinja2
app.jinja_env.filters['enumerate'] = jinja2_enumerate

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke_text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username
            return redirect(url_for('jokes'))
    return render_template('signin.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/jokes')
def jokes():
    if 'username' in session:
        user_id = User.query.filter_by(username=session['username']).first().id
        jokes = Joke.query.filter_by(user_id=user_id).all()
        joke_texts = [joke.joke_text for joke in jokes]
        return render_template('jokes.html', jokes=joke_texts)
    return redirect(url_for('index'))

@app.route('/generate_joke')
def generate_joke():
    joke_response = requests.get('https://api.chucknorris.io/jokes/random')
    joke_text = joke_response.json()['value']
    if 'username' in session:
        user_id = User.query.filter_by(username=session['username']).first().id
        new_joke = Joke(joke_text=joke_text, user_id=user_id)
    else:
        new_joke = Joke(joke_text=joke_text)
    db.session.add(new_joke)
    db.session.commit()
    
    # Get the latest joke from the database
    latest_joke = Joke.query.order_by(Joke.timestamp.desc()).first()
    
    # Get all jokes from the database
    all_jokes = Joke.query.all()

    return render_template('jokes.html', latest_joke=latest_joke, jokes=all_jokes)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000, debug=True)