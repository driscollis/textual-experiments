from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP,  SMTPRecipientsRefused


mail_server = "smtp.ISP.com"
mail_port = 587
sender_email = "mike@googoo.com"

to_addresses =  ["SOME_ADDRESS"]

with SMTP(mail_server, mail_port) as server:
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = ", ".join(to_addresses)
    msg["Subject"] = "Test 2 from Python"
    msg.attach(MIMEText("blah blah blah", "plain"))
    try:
        server.sendmail(sender_email, to_addresses, msg.as_string())
    except SMTPRecipientsRefused:
        print("NEED TO USE AUTH!!!")
        server.starttls()
        server.login(sender_email, "PASSWORD")
        server.sendmail(sender_email, to_addresses, msg.as_string())


