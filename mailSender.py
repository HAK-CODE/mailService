import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail:
    def send_mail(self, subject, message, sendersList=[], ccList=[]):
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = 'hammad4898@gmail.com'
            msg['To'] = ', '.join(sendersList)
            msg['Cc'] = ', '.join(ccList)
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('email', 'password')
            server.sendmail('hammad4898@gmail.com', sendersList+ccList, msg.as_string())
            print("Successfully sent email")
            server.quit()
        except smtplib.SMTPException:
            print("Error: unable to send email")

