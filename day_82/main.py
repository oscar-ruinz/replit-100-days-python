from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/language', methods=["GET"])
def language():
  get = request.args

  if get == {}:
    return "Nothing Here"
  if get["lang"].lower() == "esp":
     return "Hola máquinas del chambeo"
  elif get["lang"].lower() == "eng":
    return "Hello, and welcome to this awesome page!!"
  else:
    return "Unsupported language"

@app.route('/')
def index():
  return redirect('http://127.0.0.1:5000/language')

