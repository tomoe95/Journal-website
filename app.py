import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///data.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    user_id = session["user_id"]

    if request.method == "GET":
        return render_template("new_main_page.html")

    if request.method == "POST":
        date = request.form.get("date")
        feeling = request.form.get("feeling")
        description = request.form.get("description")

        if len(date) != 10:
            return apology("must provide correct year")

        db.execute("INSERT INTO journals (user_id, date, feeling, description) VALUES(?, ?, ?,?)",
                    user_id, date, feeling, description)

    return redirect("/history")


@app.route("/history")
@login_required
def calendar():
    user_id = session["user_id"]

    data = db.execute(
        "SELECT date, feeling, description FROM journals WHERE user_id = ? ORDER BY date desc", user_id)
    return render_template("history.html", data=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session.clear()

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("login.html")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return render_template("new_main_page.html", username=username)


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        birth = request.form.get("birth")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        check = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(check) != 0:
            return apology("username is already taken")

        if password != confirm:
            return apology("could not confirm password")

        if len(birth) != 10:
            return apology("must provide correct birth year")

        hash = generate_password_hash(password)

        db.execute("INSERT INTO users (first_name, last_name, birth, username, hash) VALUES(?, ?, ?, ?, ?)",
                    first_name, last_name, birth, username, hash)

        return redirect("/login")


@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "GET":
        return render_template("forget.html")

    if request.method == "POST":
        username = request.form.get("username")
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirm = request.form.get("confirm")

        if new_password != confirm:
            return apology("could not confirm password")

        check = db.execute("SELECT username, hash FROM users WHERE username = ?", username)

        if len(check) != 1:
            return apology("username does not exist")

        if not check_password_hash(check[0]["hash"], old_password) or username in check:
            return apology("user does not exist. is your information correct?")

        hash = generate_password_hash(new_password)

        db.execute("UPDATE users SET hash = ? WHERE username = ?",
                    hash, username)

        return redirect("/login")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
