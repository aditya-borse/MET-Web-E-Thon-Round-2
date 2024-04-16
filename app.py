from cs50 import SQL
from flask import Flask, render_template, request, session, redirect
from flask_session import Session

# Configuring the application
app = Flask(__name__)

# database
db = SQL("sqlite:///database.db")

# Configuring the session
app.config["SESSION_PERMENENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
  return render_template("index.html")


@app.route("/book-a-table", methods=["POST"])
def book():
  # Get the form data
  name = request.form.get("name")
  email = request.form.get("email")
  phone = request.form.get("phone")
  date = request.form.get("date")
  time = request.form.get("time")
  people = request.form.get("people")
  db.execute("INSERT INTO bookings (name, email, phone, date, time, people)")
  return render_template("booking-confirmation.html")
             
if __name__ == '__main__':
  app.run(debug=True)

