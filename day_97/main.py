from openai import OpenAI
from bs4 import BeautifulSoup
import os
import requests
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")

def summarizeArticle(article):

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=f"""Eres un escritor experto, especializado en realizar resumenes de artículos, Te voy a compartir un articulo con formato de pagina web(HTML).
            Tu trabajo es hacer un resumen de este articulo y estructurarlo en: idea principal y puntos claves.
            Articulo: {article}"""
    )

    return response.output_text




import requests

url = "https://dev.to/oscar-ruinz/la-ia-no-te-va-a-quitar-el-trabajo-pero-un-desarrollador-que-sepa-como-usarla-si-lo-hara-2bin"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

article = soup.find_all("div", {"class":"article-wrapper"})

print(summarizeArticle(article))