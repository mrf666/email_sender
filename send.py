import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import files
from time import sleep
import sys


def send_mail(header, text): 
   fromaddr = ""
   toaddr = files.get_emails()
   #Настройки > 
   mypass = ""
   app_pass = ""
   for i in range(len(toaddr)):
      msg = MIMEMultipart()
      msg['From'] = fromaddr
      msg['To'] = toaddr[i]
      msg['Subject'] = header
      msg['attach']

      
      body = text
      msg.attach(MIMEText(body, 'plain'))

       
      server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
      server.login(fromaddr, mypass)
      text = msg.as_string()
      server.sendmail(fromaddr, toaddr[i], text)
      server.quit()
#kh0jh09au9y0oko0b309tjituy86


def timechech(check):
   now = datetime.now()

   current_time = now.strftime("%H:%M")
   time_to_send = "19:42"
   print("Current Time is :", current_time)
   if current_time==time_to_send:
      print("Current Time is :", current_time)
     # send_mail("Test","test\n\n\ntest\ty")
      send_mail("WOWO","Bu")
      sys.exit(0)

def main():
   check = True
   while check:
      timechech(check)
      sleep(30)


if __name__ == '__main__':
   main()
