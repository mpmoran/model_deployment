import random
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/roll-dice")
def roll_dice():
    return str(random.randint(1, 6))
