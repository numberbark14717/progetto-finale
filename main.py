from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/linea-tempo")
def linea_tempo():
    return render_template("lineatempo.html")

@app.route("/edciv")
def edciv():
    return render_template("edciv.html")

@app.route("/edfis-irc")
def edfis_irc():
    return render_template("edfis-irc.html")

@app.route("/ing-spa")
def ing_spa():
    return render_template("ing-spa.html")

@app.route("/ita-sto-geo")
def ita_sto_geo():
    return render_template("ita-sto-geo.html")

@app.route("/mat-sci-tec")
def mat_sci_tec():
    return render_template("mat-sci-tec.html")

@app.route("/mus-art")
def mus_art():
    return render_template("mus-art.html")

if __name__ == "__main__":
    app.run(debug=True)
