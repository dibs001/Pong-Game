import smtplib
#importing from encoder module from email package
from email import encoders
# importing MIMEText class from email.mime.text module
from email.mime.text import MIMEText
#for attachment
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server=smtplib.SMTP('smtp.gmail.com',25)#defining smtp server,port
# server.connect("smtp.gmail.com",465)
server.ehlo()
# server.starttls()
with open('password.txt','r') as f:
    password=f.read()
server.login('testmail@gmail.com',password)
msg=MIMEMultipart()
msg['From']='testmail@gmail.com'
msg['To']='testmail@gmail.com'
msg['Subject']='Hellooooo'

with open('message.txt','r') as f:
    message = f.read()
msg.attach(MIMEText(message,'plain'))#attaching header and text to msg object

filename='Sea.png'
attachment= open(filename,'rb')#opening filename for reading  filename content in binary format(rb)
# payload obj (p)
p=MIMEBase('application','octet-stream')#to process the application(img here)
p.set_payload(attachment.read())

encoders.encode_base64(p)# encoding info
# payloads are declared within{}
p.add_header('Content-Disposition', f'attachment;filename{filename}')#multiple parameters are separated by ';'
msg.attach(p)#attaching payload to the msg

text=msg.as_string()# converting msg to a string
# sending mail by the server
server.sendmail('testmail@gmail.com','testmail@gmail.com',text)
# server.quit()