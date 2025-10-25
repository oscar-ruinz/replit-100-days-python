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

bd = {}
bd["Keychron M6 Wireless Mouse"] = {"normalPrice": 1461.99, "thresholdPrice":1000.0}
bd["Keychron K13 Pro QMK/VIA Wireless Custom Mechanical Keyboard ISO Layout Collection"] = {"normalPrice": 3269.99, "thresholdPrice":2500.0}
bd["Keychron B1 Pro Ultra-Slim Wireless Keyboard ISO Layout Collection"] = {"normalPrice": 1327.99, "thresholdPrice":900.0}
bd["Keychron Q4 QMK Custom Mechanical Keyboard ISO Layout Collection"] = {"normalPrice": 4822.99, "thresholdPrice":3500.0}



def scrapPage():
    urls = ["https://www.keychron.mx/products/keychron-m6-wireless-mouse?variant=52182628073685","https://www.keychron.mx/collections/keychron-iso-jis-keyboard-collection/products/keychron-k13-pro-qmk-via-wireless-custom-mechanical-keyboard-iso-layout-collection","https://www.keychron.mx/collections/keychron-iso-jis-keyboard-collection/products/keychron-b1-pro-ultra-slim-wireless-keyboard-iso-layout-collection","https://www.keychron.mx/products/keychron-q4-qmk-custom-mechanical-keyboard-iso-layout-collection"]
    #url = "https://www.keychron.mx/products/keychron-m6-wireless-mouse?variant=52182628073685"
    for url in urls:
        response = requests.get(url)
        html = response.text
    
        soup = BeautifulSoup(html, 'html.parser')
    
        myLinks = soup.find_all("div", {"class":"product-info__price"})
        title = soup.find("h1",{"class":"product-title"})
        productName = title.text.strip()
        
        price = myLinks[0].find("span", {"class":"js-value"})
        formatPrice = price.text.replace("MXN$ ","")
        formatPrice = float(formatPrice.replace(",",""))
        offerPrice = bd[productName]["thresholdPrice"]
        normalPrice = bd[productName]["normalPrice"]
        
        if formatPrice <= offerPrice:
            sendMail(f"Producto {productName} en descuento, de ${normalPrice} a ${offerPrice}")


def sendMail(message):
  email = message
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 

  msg = MIMEMultipart() 
  msg['To'] = email 
  msg['From'] = username 
  msg['Subject'] = 'Nueva oferta :D'
  msg.attach(MIMEText(email, 'html'))

  s.send_message(msg) 
  del msg 


def runSchedule():
  print("Scraping page")
  scrapPage()

schedule.every(24).hours.do(runSchedule)

while True:
  schedule.run_pending()
  time.sleep(1)