# importacao da biblioteca de smtp 
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = ''
PASSPWORD = ''

smtp = smtplib.SMTP(host='smtp-mail.outlook.com', port='587')
smtp.starttls()
smtp.login(MY_ADDRESS, PASSPWORD)

def send_email(name, email, name_sorteado):
    msg = MIMEMultipart()

    message = f'''Olá! {name}
    A pessoa que você retirou no sorteio foi a {name_sorteado}      
    '''

    msg['From'] = MY_ADDRESS
    msg['To'] = email
    msg['Subject'] = "Sorteio de Amigo Secreto"

    msg.attach(MIMEText(message, 'plain'))

    smtp.send_message(msg)
