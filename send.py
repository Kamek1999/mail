import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

content = 'ecample email stuff here'
my_email = "pythoninsta1@gmail.com"
to_email = "kamek1999@gmail.com"
password = "dvdromkamek1"
mail = smtplib.SMTP('smtp.gmail.com', 587)
suffix = ".png"

try:
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = to_email
    msg['Subject'] = r"Charts\April20.png"
    body = "chart - "
    msg.attach(MIMEText(body, 'plain'))
    filename = "Charts\April20" + suffix
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(part)
    text = msg.as_string()
    mail.ehlo()
    mail.starttls()
    mail.login(my_email, password)
    mail.sendmail(my_email, to_email, text)
    mail.close()
    print("E-mail sended")
except Exception as e:
    print(e)
    print("Couldnt send")
