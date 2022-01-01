import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading


def send_mail_toadmins(mail_from, concern, phone, email_id, admin_mails, subject="You got a message from AILobby",
                       sender_email="ailobby2021@gmail.com",
                       password="IAMIronman-3000"):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    text = f"""\
    Message from {mail_from}
    His concern is :
    {concern}
    You can call him on {phone}
    You can mail him at {email_id}
    """

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        for receiver_email in admin_mails:
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
