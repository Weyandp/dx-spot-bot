from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "supersecretkey")

ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS = os.getenv("ADMIN_PASS", "dxadmin2025")

def db_connect():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["user"] == ADMIN_USER and request.form["pass"] == ADMIN_PASS:
            session["admin"] = True
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("admin"):
        return redirect(url_for("login"))
    conn = db_connect()
    spots = conn.execute("SELECT * FROM spots ORDER BY ts DESC LIMIT 50").fetchall()
    return render_template("dashboard.html", spots=spots)

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("login"))
