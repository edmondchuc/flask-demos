# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SECRET_KEY'] = 'a-very-insecure-secret'

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('index.html', user=current_user)


@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html', user=current_user)


@app.route('/login')
def login():
    user = User.query.filter_by(username='edmond').first()
    if not user:
        user = User(username='edmond')
        db.session.add(user)
        db.session.commit()
    
    login_user(user)
    return render_template('index.html', message=f'Logged in!', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html', message='Logged out!')
