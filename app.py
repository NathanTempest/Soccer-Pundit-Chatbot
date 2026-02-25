from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")

def index():
    # name = request.args.get("name")
    return render_template("index.html")


@app.route("/greet")

def greet():
    name = request.args.get("name")
    return render_template("greet.html", name=name)
