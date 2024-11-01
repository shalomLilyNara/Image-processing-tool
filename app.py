from flask import Flask, render_template, request, redirect
from PIL import Image
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/convert", methods=["POST", "GET"])
def convert():
    if request.method == "POST":
        file = request.files["image"]
        format = request.form.get("format")
    return render_template("convert.html")

@app.route("/removeBG", methods=["POST", "GET"])
def removeBG():
    if request.method == "POST":
        file = request.files["image"]
        format = request.form.get("format")
    return render_template("removeBG.html")