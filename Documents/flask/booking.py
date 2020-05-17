import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgres://postgres:123456@localhost:5432")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index ():
	flights = db.execute("SELECT * FROM flight").fetchall()
	return render_template("booking.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
	name = request.form.get("name")
	try:
		flight_id = int(request.form.get("flight_id"))
	except ValueError:
		return render_template("error.html", message="invalid flight id")

	if db.execute("SELECT * FROM flight WHERE id = :id", {"id": flight_id}).rowcount == 0:
		return render_template("error.html", message="invalid flight id")
	db.execute("INSERT INTO passenger(name, flight_id) VALUES (:name, :flight_id)",
		{"name": name, "flight_id": flight_id})
	db.commit()
	return render_template("success.html")



