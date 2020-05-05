'''
Simple Mail Spoofer
Created By Milad Khoshdel & Morteza Amirmohseni
Website: https://www.regux.com
Email: miladkhoshdel@gmail.com
'''

import smtplib, ssl

print("\n")
smtp_server = input("Enter SMTP Address: ")
port = 25  # For starttls
sender_email = input("Enter Sender Address: ")
receiver_email = input("Enter Receiver Address: ")
subject = input("Enter Subject:")
secure_connection = bool(input("Secure Connection? True/False? "))
message_data= input("Enter your message:")
message = "To:" + receiver_email + "\nFrom:" + sender_email + "\nsubject:" + subject + "\n\n" + message_data;
server = smtplib.SMTP(smtp_server,port)
# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if secure_connection:
        server.starttls()
        server.ehlo()
    server.sendmail(sender_email, receiver_email, message)
    print("\nMessage Sent Successfully.")
except Exception as e:
    print(e)
finally:
    server.quit() 
