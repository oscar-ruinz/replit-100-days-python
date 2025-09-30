from openai import OpenAI
import requests, json, os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def summarizeNews(newsContent):

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=f"Eres un periodista experto en redacción resume la siguiente noticia en una sentencia de 100 palabras. Noticia: {newsContent}"
    )

    return response.output_text


newsKey = os.getenv('NEWS_API_KEY')
country = "us"

url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"

result = requests.get(url)
data = result.json()

x = 0

for article in data['articles']:
  if x < 5:
    print(article['title'])
    resumen = summarizeNews(article['content'])
    print(f"Resumen: {resumen}")
    print()
  else:
     break
  x += 1