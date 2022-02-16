from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Hotel_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Valstis(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  valsts = db.Column(db.String(60), nullable=False)
  saisinajums = db.Column(db.String(10))
  viesnic_sk = db.Column(db.Integer)
  #children = db.relationship("Viesnicas", cascade="all, delete")
  
  def __repr__(self):
      return 'Task %r' % self.id
'''
class Viesnicas(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  #valsts_id = db.Column(db.Integer, db.ForeignKey("valsts.id"))
  nosaukums = db.Column(db.String(60))
  zvaigznes = db.Column(db.String(5))
  numurini = db.Column(db.Integer)
  cena = db.Column(db.Float)
  def __repr__(self):
    return f'<from valsts {self.valsts_id}>'

  def valsts_id_ieguve(self):
    return Valstis.query.filter(Valstis.id == self.valsts_id).first()'''


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