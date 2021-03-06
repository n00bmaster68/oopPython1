from flask import Flask, render_template, request, jsonify
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:123456@localhost:5432/QLCB"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
	flights = Flight.query.all()
	return render_template("booking.html", flights = flights)

@app.route("/book", methods=["POST"])
def book():
	name = request.form.get("name")
	try:
		flight_id = int(request.form.get("flight_id"))
	except ValueError:
			return render_template("error.html", message="invalid flight id")
	flight = Flight.query.get(flight_id)
	if flight is None:
		return render_template("error.html", message="invalid flight id")

	flight.add_passenger(name)	
	return render_template("success.html", flight_id=flight_id, flight=flight)	

@app.route("/flights")
def flights():
	flights = Flight.query.all()
	return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
	flight = Flight.query.get(flight_id)
	if flight is None:
		return render_template("error.html", message="invalid flight id")

	passengers = flight.passengers
	return render_template("flight1.html", flight=flight, passengers=passengers)

@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
	flight = Flight.query.get(flight_id)
	if flight is None:
		return jsonify({"error": "Invalid flight_id"}), 422

	passengers = flight.passengers
	names = []
	for passenger in passengers:
		names.append(passenger.name)
	return jsonify({
		"origin": flight.origin,
		"destination": flight.destination,
		"duration": flight.duration,
		"passengers": names
		})
