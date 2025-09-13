from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index(): 
  page = f"""<html><body>
  <h1>My Blog</h1>
  <ul>
  <li><a href="/helloworld">Hello World</a></li>
  <li><a href="/holamundo">Hola Mundo</a></li>
  </ul>
  </body>
  </html>"""
  return page


@app.route('/1')
def shortenerOne():
    return redirect('http://127.0.0.1:5000/helloworld')


@app.route('/2')
def shortenerTwo():
    return redirect('http://127.0.0.1:5000/holamundo')

@app.route('/helloworld')
def hello():
    title = "Hello World!"
    date = "September 13th, 2025"
    text = "Here is my first blog entry."

    page = ""
    f = open("template/blog.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{name}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    return page


@app.route('/holamundo')
def hola():
    title = "Hola Mundo!"
    date = "13 de Septiembre, 2025"
    text = "Mi primera entrada en el blog."

    page = ""
    f = open("template/blog.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{name}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    return page