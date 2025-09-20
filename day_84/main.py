from flask import Flask, request, redirect
from replit import db


app = Flask(__name__, static_url_path='/static')

@app.route('/login', methods=["POST"])
def login():
  form = request.form
  try:
    if db[form["username"]]["password"] == form["password"]:
      return f"<h1>Hello {form['username']}</h1>"
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
  page = readTemplate("templates/index.html")
  return page

def readTemplate(path):
  content = ""
  f = open(path, "r")
  content = f.read()
  f.close()
  return content
