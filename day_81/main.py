from flask import Flask, request

app = Flask(__name__)

@app.route('/questionsForm', methods=["POST"])
def questionForm():
  humanTemplate = readTemplate("./templates/humanUser.html")
  robotTemplate = readTemplate("./templates/robotUser.html")
  form = request.form
  if form["question1"] == "yes" or form["question2"] != "infinity" or form["question3"] == "information":
    return robotTemplate
  else:
    return humanTemplate

  
@app.route('/')
def index():
  f = open("./templates/questionsForm.html", "r")
  page = f.read()
  f.close()
  return page


def readTemplate(fileRoute):
  f = open(fileRoute, "r")
  template = f.read()
  f.close()
  return template