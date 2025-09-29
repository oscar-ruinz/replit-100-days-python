import requests, json, os
from requests.auth import HTTPBasicAuth
from flask import Flask, request, redirect, session
from replit import db

app = Flask(__name__)

def searchSongs(year):
  clientID = os.environ['CLIENT_ID']
  clientSecret = os.environ['CLIENT_SECRET']

  url = "https://accounts.spotify.com/api/token"
  data = {"grant_type":"client_credentials"}
  auth = HTTPBasicAuth(clientID, clientSecret)

  response = requests.post(url, data=data, auth=auth)
  accessToken = response.json()["access_token"]

  url = "https://api.spotify.com/v1/search"
  headers = {'Authorization': f'Bearer {accessToken}'}
  search = f"?q=year%3A{year}&type=track&limit=20&offset=0"

  fullURL = f"{url}{search}"

  response = requests.get(fullURL, headers=headers)
  data = response.json()
  content = ""
  for track in data["tracks"]["items"]:
      content += f"""<h2>{track['name']}</h2><audio controls><source src="{track['preview_url']}" type="audio/mpeg"></audio><hr>"""
    
  return content

@app.route('/', methods=["GET"])
def index():
  data = request.args
  
  songs = "" if data == {} else searchSongs(data["year"])
    
  page = readTemplate("index.html")
  page = page.replace("{{songs}}",songs)
  
  return page


def readTemplate(path):
  content = ""
  f = open(path, "r")
  content = f.read()
  f.close()
  return content


app.run(host='0.0.0.0', port=81)
