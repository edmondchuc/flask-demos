# app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    items = ['code', 'python', 'web', 'flask', 'html', 'jinja']
    return render_template('index.html', title='Jinja for loop demo!', items=items)
