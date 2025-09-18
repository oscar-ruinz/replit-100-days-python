from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index(): 
  page = f"""<html><body>
  <h1>My Blog</h1>
  <ul>
  <li><a href="/hello?template=default">Hello World!</a></li>
  </ul>
  </body>
  </html>"""
  return page

@app.route('/hello', methods=["GET"])
def hello():
    title = "Hello World!"
    date = "September 13th, 2025"
    text = "Here is my first blog entry."

    data = request.args

    page = ""
    f = open("template/blog.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{{name}}", title)
    page = page.replace("{{date}}", date)
    page = page.replace("{{text}}", text)

    if data != {}:
        if data["template"].lower() == "red":
           page = page.replace("{{color}}", "#da5252")
        elif data["template"].lower() == "blue":
           page = page.replace("{{color}}","#2a5cc7")
        elif data["template"].lower() == "green":
           page = page.replace("{{color}}","#68dc42")
        else:
           page = page.replace("{{color}}","#FFF")



    return page
