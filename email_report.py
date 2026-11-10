import smtplib

def send_report(report_text):

    sender = "yourgmail@gmail.com"
    password = "gmail-app-password"

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(
        sender,
        password
    )

    server.sendmail(
        sender,
        "vos.anastasija@gmail.com",
        report_text
    )

    server.quit()
