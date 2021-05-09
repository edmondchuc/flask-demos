# app.py
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return {'message': 'success'}
