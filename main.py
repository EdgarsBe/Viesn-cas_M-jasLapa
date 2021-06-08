from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def Homepage():
  return render_template("Homepage.html")


@app.route('/Logged-In')
def LoggedInPage():
  return render_template("Ielogojies_Lapa.html")

@app.route('/Admin-Page')
def AdminPage():
  return render_template("Admin_Homepage.html")

@app.route('/Rezervēšana')
def Rezervet():
  return render_template("rezervacijas.html")

@app.route('/Admin-Rediģēšana')
def Rediget():
  return render_template("Admin_Viesnīcu_Rediģēšana.html")

@app.route('/Veiktas-Rezervacijas')
def VeiktasRezervacijas():
  return render_template("veikto_rezervaciju_lapa.html")

@app.route('/tabula')
def Tabula():
  return render_template("tabula.html")

@app.route('/Admin-Statistikas-Lapa')
def Statistika():
  return render_template("Admin_Statistikas_Lapa.html")



app.run(host='0.0.0.0', port=8080)