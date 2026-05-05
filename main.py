from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/linea-tempo")
def linea_tempo():
    return render_template("lineatempo.html")

app.run()