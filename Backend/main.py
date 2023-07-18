from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import config

app = FastAPI()


class Email(BaseModel):
    subject: str
    message: str
    recipients: list[EmailStr]


@app.post("/send_email")
async def send_email(email: Email):
    # Create the message
    message = MIMEMultipart()
    message["From"] = config.email
    message["Subject"] = Header(email.subject)

    # Attach the email body
    body = MIMEText(email.message, "plain")
    message.attach(body)

    # Convert the recipients to a comma-separated string
    recipients = ','.join(email.recipients)

    try:
        # Connect to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            # Start TLS encryption
            server.starttls()
            # Login to your Google email account
            server.login(config.email, config.password)
            # Send the email
            server.sendmail(config.email, recipients.split(','), message.as_string())

        return {"message": "Email sent successfully!"}
    except Exception as e:
        return {"message": f"Error sending email: {str(e)}"}
