import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SMTP:
    def __init__(self):
        with open('smtpsettings.json') as f:
            settings = json.load(f)

        self.email = settings['email']
        self.password = settings['password']
        self.server = settings['server']
        self.port = settings['port']
        self.server = smtplib.SMTP(self.server, self.port)

    def send(self, to, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        self.server.starttls()
        self.server.login(self.email, self.password)
        self.server.sendmail(self.email, to, msg.as_string())
        self.server.quit()
