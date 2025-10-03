import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("span", {"class":"titleline"})

for link in myLinks:
    if "n8n" in link.text.lower() or "apple" in link.text.lower():
        print(link.text)
