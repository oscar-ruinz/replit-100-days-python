from flask import Flask, request

app = Flask(__name__)

validUsers = {
  "oscar": "hola",
  "rodrigo": "rodrigo",
  "regina": "regina"
}
print(validUsers["oscar"])

@app.route('/login', methods=["POST"])
def login():
  invalidUserTemplate = readTemplate("./templates/invalidUser.html")
  validUserTemplate = readTemplate("./templates/validUser.html")
  form = request.form
  if form["username"] in validUsers.keys() and form["password"] == validUsers[form["username"]]:
    validUserTemplate = validUserTemplate.replace("{{username}}",form["username"])
    return validUserTemplate
  else:
    return invalidUserTemplate

  
@app.route('/')
def index():
  f = open("./templates/loginForm.html", "r")
  page = f.read()
  f.close()
  return page


def readTemplate(fileRoute):
  f = open(fileRoute, "r")
  template = f.read()
  f.close()
  return template