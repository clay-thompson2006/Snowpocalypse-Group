import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#Gmail Parameters
def Alert():
    sender_email = "phillips_clayton@student.mahoningctc.com"
    recipient_email = "phillips_clayton@student.mahoningctc.com"
    #recipient_email = "michael.sekol@mahoningctc.com"
    subject = "Snow Day Alert"
    message = "Mr. Sekol This is your alarm to tell you that there might be a snow day so have fun with the puppers and have a great day."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # 587 is the TLS/STARTTLS port for Gmail

    # Create an SMTP session
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable TLS encryption

    email_password = "Arm70dust"
    server.login(sender_email, email_password)

    server.sendmail(sender_email, recipient_email, msg.as_string())

    server.quit()
