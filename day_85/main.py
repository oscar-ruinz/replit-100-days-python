from flask import Flask, request, redirect, session
from replit import db
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.environ['SESSION_SECRET']


@app.route('/login', methods=["POST"])
def login():
  form = request.form
  try:
    if db[form["username"]]["password"] == form["password"]:
      name = ""
      if session.get("myName"):
        name = session["myName"]
      else:
        name = form["username"]
        session["myName"] = request.form["username"]
      page = readTemplate("templates/hello.html")
      page = page.replace("{{{username}}}", name)
      return page
    else:
      return redirect("/")
  except Exception:
    return redirect("/")


@app.route('/register', methods=["POST"])
def register():
  form = request.form
  if form["username"] in db.keys():
    return """<p>User already exists!</p><a href="/">Return to home</a>"""
  else:
    db[form["username"]] = {"password": form["password"],"name": form["name"]}
    return redirect("/login-page")

@app.route("/login-page")
def login_page():
  page = readTemplate("templates/login.html")
  return page

@app.route("/sign-up")
def sign_up():
  page = readTemplate("templates/sign-up.html")
  return page

@app.route('/')
def index():
  if not session.get("myName"):
    return redirect("/login-page")
  page = readTemplate("templates/index.html")
  return page

@app.route("/reset", methods=["POST"])
def reset():
  session.clear()
  return redirect("/login-page")

def readTemplate(path):
  content = ""
  f = open(path, "r")
  content = f.read()
  f.close()
  return content
