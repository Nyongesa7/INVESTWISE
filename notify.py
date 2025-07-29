import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

# ======================
# 📬 EMAIL NOTIFICATIONS
# ======================

def send_email_alert(recipient_email, subject, body, sender_email, sender_password):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print(f"✅ Email sent to {recipient_email}")
    except Exception as e:
        print(f"❌ Email failed: {e}")


# =========================
# 📱 WHATSAPP NOTIFICATIONS
# =========================

def send_whatsapp_alert(to_number, message, twilio_sid, twilio_token, from_whatsapp='+14155238886'):
    try:
        client = Client(twilio_sid, twilio_token)
        message = client.messages.create(
            from_='whatsapp:' + from_whatsapp,
            body=message,
            to='whatsapp:' + to_number
        )
        print(f"✅ WhatsApp message sent: {message.sid}")
    except Exception as e:
        print(f"❌ WhatsApp failed: {e}")
