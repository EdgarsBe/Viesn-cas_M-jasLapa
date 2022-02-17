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
  saisinajums = db.Column(db.String(10), nullable=False)
  viesnic_sk = db.Column(db.Integer, nullable=False)
  
  def __repr__(self):
      return 'Task %r' % self.id

class Viesnicas(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  valsts_iz = db.Column(db.String(200), nullable=False)
  nosaukums = db.Column(db.String(60), nullable=False)
  zvaigznes = db.Column(db.String(5), nullable=False)
  numurini = db.Column(db.Integer, nullable=False)
  cena = db.Column(db.Float, nullable=False)

  def __repr__(self):
      return 'Viesnic %r' % self.id

class Rezervacijas(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  valsts = db.Column(db.String(60), nullable=False)
  nosaukums = db.Column(db.String(60), nullable=False)
  zvaigznes = db.Column(db.String(5), nullable=False)
  DatumsNo = db.Column(db.String(200), nullable=False)
  DatumsLidz = db.Column(db.String(200), nullable=False)

  def __repr__(self):
      return 'Rezervacij %r' % self.id

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
  return render_template("Rediģēšana(admin).html")

#Rezervācijas klientu pusē.

@app.route('/Veiktas-Rezervacijas', methods=['POST', 'GET'])
def Rezervacij_func():
  if request.method == 'POST':
    jauna_rezervacija = Rezervacijas(valsts=request.form['valsts'],
    nosaukums=request.form['nosaukums'], zvaigznes=request.form['zvaigznes'], DatumsNo=request.form['DatumsNo'], DatumsLidz=request.form['DatumsLidz'],)
    try:
        db.session.add(jauna_rezervacija)
        db.session.commit()
        return redirect('/Veiktas-Rezervacijas') 
    except:
        return 'Kļūda!'
  else:
    valstis = Valstis.query.order_by(Valstis.id).all()
    viesnicas = Viesnicas.query.order_by(Viesnicas.id).all()
    rezervacijas = Rezervacijas.query.order_by(Rezervacijas.id).all()
    return render_template('Rezervācijas_veikšana.html', valstis=valstis, viesnicas=viesnicas, rezervacijas=rezervacijas)


#Admin Viesnīcu Reiģēšanas Lapas Funkcijas un DB.

@app.route('/Admin-Rediģēšana/Viesnicas', methods=['POST', 'GET'])
def Viesnicas_func():
  if request.method == 'POST':
    jauna_viesnica = Viesnicas(valsts_iz=request.form['valsts_iz'], nosaukums=request.form['nosaukums'],zvaigznes=request.form['zvaigznes'], numurini=request.form['numurini'], cena=request.form['cena'])
    try:
        db.session.add(jauna_viesnica)
        db.session.commit()
        return redirect('/Admin-Rediģēšana/Viesnicas')
    except:
        return 'Kļūda pievienojot Viesnicu!'
  else:
    valstis = Valstis.query.order_by(Valstis.id).all()
    tasks = Viesnicas.query.order_by(Viesnicas.id).all()
    return render_template('Viesnicu_tabula.html', valstis=valstis, tasks = tasks)

@app.route('/izdzest_Viesnicas/<int:id>')
def Viesnicas_izdzest(id):
    task_to_delete = Viesnicas.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/Admin-Rediģēšana/Viesnicas')
    except:
        return 'nesanāca izdzēst'  

@app.route('/Admin-Rediģēšana/Viesnicas/update/<int:id>', methods=['GET', 'POST'])
def Update_Viesnicas(id):
    task = Viesnicas.query.get_or_404(id)
    if request.method == 'POST':
        task.valsts_iz = request.form['valsts_iz']
        task.nosaukums = request.form['nosaukums']
        task.zvaigznes = request.form['zvaigznes']
        task.numurini = request.form['numurini']
        task.cena = request.form['cena']
        try:
            db.session.commit()
            return redirect('/Admin-Rediģēšana/Viesnicas')
        except:
            return "Kļūda veicot labojumu!"
    else:
        valstis = Valstis.query.order_by(Valstis.id).all()
        return render_template("Update_Viesnicas.html", task=task, valstis=valstis)

#Admin Valsts Reiģēšanas Lapas Funkcijas un DB.

@app.route('/Admin-Rediģēšana/Valstis', methods=['POST', 'GET'])
def Valstis_func():
    if request.method == 'POST':
      jauna_valsts = Valstis(
      valsts=request.form['valsts'],
      saisinajums=request.form['saisinajums'],
      viesnic_sk=request.form['viesnic_sk'])
      
      try:
        db.session.add(jauna_valsts)
        db.session.commit()
        return redirect('/Admin-Rediģēšana/Valstis')
      except:
        return 'Kļūda pievienojot Valsti!'

    else:
      tasks = Valstis.query.order_by(Valstis.id).all()
      return render_template('Valsts_tabula.html', tasks=tasks)

@app.route('/izdzest_Valsts/<int:id>')
def Valsts_izdzest(id):
    task_to_delete = Valstis.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/Admin-Rediģēšana/Valstis')
    except:
        return 'Nesanāca izdzēst!'      

@app.route('/Admin-Rediģēšana/Valstis/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Valstis.query.get_or_404(id)
    if request.method == 'POST':
        task.valsts = request.form['valsts']
        task.saisinajums = request.form['saisinajums']
        task.viesnic_sk = request.form['viesnic_sk']
        try:
            db.session.commit()
            return redirect('/Admin-Rediģēšana/Valstis')
        except:
            return "Kļūda veicot labojumu!"
    else:
        return render_template("Update_Valsts.html", task=task)


if __name__ == "__main__": 
  app.run(host='0.0.0.0', port=8000)
