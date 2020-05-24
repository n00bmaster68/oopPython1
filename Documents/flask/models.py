from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
	__tablename__="flights"
	id = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String, nullable=True)
	destination = db.Column(db.String, nullable=True)
	duration = db.Column(db.Integer, nullable=True)
	passengers = db.relation("Passenger", backref="flight", lazy=True)

	def add_passenger(self, name):
		p = Passenger(name=name, flight_id=self.id)
		db.session.add(p)
		db.session.commit()

class Passenger(db.Model):
	__tablename__="passengers"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=True)
	flight_id = db.Column(db.Integer,db.ForeignKey("flights.id"), nullable=True)


