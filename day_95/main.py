from openai import OpenAI
import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
newsKey = os.getenv('NEWS_API_KEY')
country = "us"

def summarizeTitle(title):

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=f"""You are an expert headline summarizer. Summarize the following news title into a short 2-3 word phrase. 
                Use only plain text, no decoration, no punctuation, no hyphens, and no extra words like "summary" or "title". 
                Return only the phrase itself in lowercase.
                Title: {title}"""
    )

    return response.output_text

def searchSong(searchTerm):
  clientID = os.environ['CLIENT_ID']
  clientSecret = os.environ['CLIENT_SECRET']

  url = "https://accounts.spotify.com/api/token"
  data = {"grant_type":"client_credentials"}
  auth = HTTPBasicAuth(clientID, clientSecret)

  response = requests.post(url, data=data, auth=auth)
  accessToken = response.json()["access_token"]

  searchTerm = searchTerm.replace(" ","%20")

  url = "https://api.spotify.com/v1/search"
  headers = {'Authorization': f'Bearer {accessToken}'}
  search = f"?q={searchTerm}&type=track&limit=1"

  fullURL = f"{url}{search}"

  response = requests.get(fullURL, headers=headers)
  data = response.json()
  content = ""
  for track in data["tracks"]["items"]:
      content += f"{track['name']}"
    
  return content


url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}&category=technology"

result = requests.get(url)
data = result.json()


articles = {}

for x, article in enumerate(data['articles']):
  if x < 5:
    phrase = summarizeTitle(article['title'])
    song = searchSong(phrase)
    articles[x] = {"title": article['title'], "phrase": phrase, "song": song}
  else:
    break

for value in articles.values():
   print(f"Title: {value['title']}\nPhrase: {value['phrase']}\nSong name: {value['song']}\n\n")
