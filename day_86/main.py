from flask import Flask, request, redirect, session
from replit import db
import os,datetime

app = Flask(__name__)
app.secret_key = os.environ['SESSION_SECRET']


@app.route('/')
def index():
  return redirect("/login-page")

@app.route('/login', methods=["POST"])
def login():
  form = request.form
  try:
    if db["user"]["password"] == form["password"] and db["user"]["username"] == form["username"]:
      if not session.get("myBlog"):
          session["myBlog"] = form["username"]
      return redirect("/blog")
    else:
      return """<h1>Wrong password or username</h1><button type="button" onclick="location.href='/login-page'">Log in</button><br><br><button type="button" onclick="location.href='/blog'">Go to Oscar's Blog</button><br><br>"""
  except Exception:
    return redirect("/login")


@app.route("/login-page")
def login_page():
  if session.get("myBlog"):
    page = readTemplate("templates/index.html")
  else:
    page = readTemplate("templates/login.html")
  return page

@app.route("/blog")
def blog_page():
  if session.get("myBlog"):
    page = readTemplate("templates/index.html")
  else:
    page = readTemplate("templates/blog.html")

  matches = db.prefix("BE")
  matches = matches[::-1]
  blogEntries = ""
  for key in matches:
    blogEntries += f"<hr><h2>{db[key]['title']}</h2><h3>{db[key]['date']}</h3><p>{db[key]['body']}</p>"
  page = page.replace("{{blog-entries}}",blogEntries)
  
  return page

@app.route("/log-out")
def logout():
  session.clear()
  return redirect("/blog")

@app.route("/new-entry", methods=["POST"])
def newEntry():
  form = request.form

  if form != {}:
    timestamp = str(datetime.datetime.now())
    key = F"BE{timestamp}"
    db[key] = {"title": form["title"],"date": form["date"],"body": form["body"]} 
    
  
  return redirect("blog")

def readTemplate(path):
  content = ""
  f = open(path, "r")
  content = f.read()
  f.close()
  return content

app.run(host='0.0.0.0', port=81)
