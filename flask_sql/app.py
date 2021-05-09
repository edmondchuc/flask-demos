# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)


class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)


@app.route('/')
def home():
    # Get the row from the counter table by its primary key.
    counter = Counter.query.get(1)
    if not counter:
        counter = Counter(count=1)
        db.session.add(counter)
        db.session.commit()
    else:
        counter.count += 1
        db.session.commit()
    return f'Counter value: {counter.count}'
