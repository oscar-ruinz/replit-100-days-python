import schedule, time, os, smtplib, random
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

password = os.environ['mailPassword']
username = os.environ['mailUsername']

def getQuote():
  f = open("quotes.txt","r")
  quotes = f.read().split("\n")
  f.close()
  randomNumber = random.randint(0,len(quotes)-1)
  return quotes[randomNumber]

def sendMail():
  email = str(getQuote())
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 

  msg = MIMEMultipart() 
  msg['To'] = "oscarvruelas@gmail.com" 
  msg['From'] = username 
  msg['Subject'] = "Quote for the Day" 
  msg.attach(MIMEText(email, 'html'))

  s.send_message(msg) 
  del msg 


sendMail()
print("Day Quote Sent")

def printMe():
  print("⏰ Sending quote of the day")
  sendMail()

schedule.every(1).days.do(printMe)

while True:
  schedule.run_pending()
  time.sleep(1)