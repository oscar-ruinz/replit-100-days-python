from email import message
from replit import db
import requests
from bs4 import BeautifulSoup
import schedule, time, os, smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 


password = os.environ['mailPassword']
username = os.environ['mailUsername']
email = os.environ['userMail']


def scrapPage():
    url = "https://webscraper.io/test-sites/e-commerce/allinone"
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    myLinks = soup.find_all("div", {"class":"card-body"})

    for link in myLinks:
        product = link.find('a',class_='title')
        title = product.get_text().strip()
        link = product.get("href")
        price = link.find('h4',class_='price').find('span').get_text()
        if "samsung" in title.toLower():
            saveProduct(title, link, price)
        
        

def saveProduct(title,link,price):
    if title not in db.keys():
        db[title] = {price: price, link: link}
        message = f'{title} for only {price} in {link}.'
        sendMail(message,title)

def sendMail(message,product):
  email = message
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 

  msg = MIMEMultipart() 
  msg['To'] = email 
  msg['From'] = username 
  msg['Subject'] = f'New offer of {product}'
  msg.attach(MIMEText(email, 'html'))

  s.send_message(msg) 
  del msg 


def runSchedule():
  print("Scraping page")
  scrapPage()

schedule.every(6).hours.do(runSchedule)

while True:
  schedule.run_pending()
  time.sleep(1)