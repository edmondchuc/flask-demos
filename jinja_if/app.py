# app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    items = ['ruby', 'python', 'c', 'c++', 'java', 'c#']
    # items = None
    return render_template('index.html', title='Jinja if statement demo', items=items)
