def send_email_alert(to_email, subject, message):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import os

    email_user = os.getenv("EMAIL_ADDRESS")
    email_pass = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_user, email_pass)
        server.sendmail(email_user, to_email, text)


def send_whatsapp_alert(to_number, message):
    from twilio.rest import Client
    import os

    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_NUMBER")

    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_='whatsapp:' + from_number,
        to='whatsapp:' + to_number
    )
