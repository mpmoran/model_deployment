import random
from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/roll-dice")
def roll_dice():
    return render_template(
        "roll_dice.html", dice_roll_result=random.randint(1, 6)
    )


@app.route("/my-first-form")
def my_first_form():
    return render_template("my-first-form.html")


@app.route("/make-greeting", methods=["POST"])
def handle_form_submission():
    name = request.form["name"]
    title = request.form["title"]

    greeting = "Hello, "

    if title != "":
        greeting += title + " "

    greeting += name + "!"

    return render_template("greeting.html", greeting=greeting)


@app.route("/spam-detector")
def spam_detector():
    return render_template("spam-detector.html")


@app.route("/classify-message", methods=["POST"])
def classify_message():
    msg = request.form["message"]

    result = predict(msg)
    text_type = "warning"
    if result == "ham":
        text_type = "success"
    elif result == "spam":
        text_type = "danger"

    return render_template(
        "classify-message.html", text_type=text_type, result=result
    )
