""" 含附件發信(gmail server) """
import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
sys.path.append('D:/python-training/0_frequent/en_decode') 
from en_decrypt import dectry

sender_email = "hueisam57@gmail.com" #------******
receiver_email = "s0972919686@outlook.com" #------****** hueisam@krtco.com.tw
 
# Create MIMEMultipart object
msg = MIMEMultipart("alternative")
msg["Subject"] = "multipart測試" #------******
msg["From"] = sender_email
msg["To"] = receiver_email

# HTML Message Part
html = """\
<html>
  <body>
    <p><b>Python Mail Test.</b>
    <br>
       This is HTML email with attachment.<br>
       Click on <a href="https://fedingo.com">Fedingo Resources</a> 
       for more python articles.
    </p>
  </body>
</html>
"""
part = MIMEText(html, "html")
msg.attach(part)


# Add Attachment
filename = "D:/python-training/Data/excel/公務汽車.xlsx" #------******
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
# Set mail headers
part.add_header(
    "Content-Disposition",
    "attachment", filename= filename
)
msg.attach(part)


# Create secure SMTP connection and send email
password = dectry('MjI5XzEzOV8yMzRfMjEwXzE3MV8yMTBfMjE3XzE3NV8xNjNfMTY3XzE1NF8yMjJfMTk1XzE0N18yMjBfMTQ5Xw==')
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, msg.as_string()
    )


# https://hackmd.io/aOOi7qS1So-AwHXlMJLxtA?edit