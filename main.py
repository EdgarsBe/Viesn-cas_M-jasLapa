from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime
from models import db, Valstis, app

@app.route('/')
def Homepage():
  return render_template("Homepage.html")

@app.route('/Logged-In')
def LoggedInPage():
  return render_template("Homepage_Pieslēdzies.html")

@app.route('/Admin-Page')
def AdminPage():
  return render_template("Admin_Homepage.html")

@app.route('/Rezervēšana')
def Rezervet():
  return render_template("Rezervācijas_veikšana.html")

@app.route('/Veiktas-Rezervacijas')
def VeiktasRezervacijas():
  return render_template("veikto_rezervaciju_lapa.html")

@app.route('/tabula')
def Tabula():
  return render_template("tabula.html")

@app.route('/Admin-Statistikas-Lapa')
def Statistika():
  return render_template("Admin_Statistikas_Lapa.html")

@app.route('/Admin-Rediģēšana')
def Rediget():
  return render_template("Viesnīcu_rediģēšana(admin).html")

@app.route('/Admin-Rediģēšana/Valstis')
def Valstis_func():
    if request.method == 'POST':
      jauna_valsts = Valstis(valsts=request.form['valsts'],saisinajums=request.form['saisinajums'],viesnic_sk=request.form['viesnic_sk'],)
      
      try:
        db.session.add(jauna_valsts)
        db.session.commit()
        return redirect('/Admin-Rediģēšana/Valstis')
      except:
        return 'Kļūda pievienojot Valsti!'

    else:
      valstis = Valstis.query.order_by(Valstis.id).all()
      return render_template('Valsts_tabula.html', valstis=valstis)

app.run(host='0.0.0.0', port=8080)