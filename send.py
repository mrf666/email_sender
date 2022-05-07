import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import files
 
fromaddr = ""
toaddr = files.get_emails()
#Настройки > 
mypass = ""
app_pass = ""
for i in range(len(toaddr)):
   msg = MIMEMultipart()
   msg['From'] = fromaddr
   msg['To'] = toaddr[i]
   msg['Subject'] = "Привет от питона"
   msg['attach']

   
   body = "HELL IN A CELL"
   msg.attach(MIMEText(body, 'plain'))

    
   server = smtplib.SMTP_SSL('smtp.mail.ru', 465)






   server.login(fromaddr, mypass)
   text = msg.as_string()
   server.sendmail(fromaddr, toaddr[i], text)
   server.quit()
#kh0jh09au9y0oko0b309tjituy86
