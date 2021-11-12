import smtplib, ssl
from email.message import EmailMessage

port = 465  
smtp_server = "smtp.gmail.com"
sender_email = "11bbcontacto@gmail.com"
receiver_email = ["oblanco2805@gmail.com","osba_28@hotmail.com"] 
password = "messi10*"

text= "Según técnico"
msg = EmailMessage()
msg.set_content(text)

msg['Subject'] = "Correo de prueba"
msg['From'] = sender_email
msg['To'] = receiver_email

contexto = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=contexto) as server:
	server.login(sender_email, password)
	server.send_message(msg)