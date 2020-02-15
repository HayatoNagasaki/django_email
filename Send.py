import smtplib, ssl

def send(smtp_server, sender_email, receiver_email, password, subject, message):
    context = ssl.create_default_context()

    message=subject+message

    # port: 465 for SSL
    with smtplib.SMTP_SSL(smtp_server, port=465, context=context) as server:
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.close()


    print("The message was successfully sent.")



if __name__=="__main__":
    smtp_server = "smtp.gmail.com"
    sender_email = "sender email"  # Enter your address
    receiver_email = "recipient"  # Enter receiver address
    password = r"your password"
    
    subject = "Subject:"+"Hi there!\n"
    
    msg = """This message was sent from Python."""
    
    send(smtp_server,
         sender_email,
         receiver_email,
         password,
         subject,
         message=msg)
    
