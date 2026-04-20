# import smtplib
# from email.mime.text import MIMEText

# SMTP_EMAIL = "yourmail@gmail.com"
# SMTP_PASS = "your_app_password"   # paste app password here

# def send_email(to_email, subject, body):
#     try:
#         msg = MIMEText(body)
#         msg["Subject"] = subject
#         msg["From"] = SMTP_EMAIL
#         msg["To"] = to_email

#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#             server.login(SMTP_EMAIL, SMTP_PASS)
#             server.send_message(msg)

#         print(f"✅ Mail sent to {to_email}")

#     except Exception as e:
#         print(f"❌ Failed to send mail to {to_email}: {e}")
# 
# 
import smtplib
from email.mime.text import MIMEText

USE_REAL_EMAIL = True

SMTP_EMAIL = "projectaiversion@gmail.com"
SMTP_PASS = "uzlmlxzrxgpuofdy"   # ✅ new one


def send_email(to_email, subject, body):

    if not USE_REAL_EMAIL:
        print("\n📧 EMAIL SIMULATION")
        print("To      :", to_email)
        print("Subject :", subject)
        print("Body    :", body)
        print("✅ Simulated email sent\n")
        return

    try:
        msg = MIMEText(body)

        msg["Subject"] = subject
        msg["From"] = SMTP_EMAIL
        msg["To"] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SMTP_EMAIL, SMTP_PASS)
            server.send_message(msg)

        print(f"✅ Mail sent to {to_email}")

    except Exception as e:
        print(f"❌ Failed to send mail to {to_email}: {e}")