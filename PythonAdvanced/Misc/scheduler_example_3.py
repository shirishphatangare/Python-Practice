import smtplib

def sendEmail(sender_email, password, to, subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        message = f'From: {sender_email}\nTo: {to}\nSubject: {subject}\n\n{msg}'
        print(message)

        server.sendmail(sender_email, to, message)
        server.quit()
        print("Email Sent")
    except:
        print("Some Error Occured")

if __name__ == '__main__':
    SENDER_EMAIL = "sample@gmail.com"
    PASSWORD = "password1"
    TO = "shynuj@gmail.com"
    SUBJECT = "Just having fun"
    MESSAGE = "hey dawg! it's my first Email"
    sendEmail(SENDER_EMAIL, PASSWORD, TO, SUBJECT, MESSAGE)
