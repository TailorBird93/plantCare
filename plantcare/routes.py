from flask import render_template
from plantcare import app, db
from plantcare.models import PlantCategory, Plant

@app.route("/")
def home():
    return render_template("plants.html")