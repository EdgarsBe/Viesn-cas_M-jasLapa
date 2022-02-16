from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db_name = 'Hotel_database.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
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