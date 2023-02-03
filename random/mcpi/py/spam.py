import smtplib,ssl


email="g4o3@protonmail.com"
password="aS77785/"



message="""\
this message is from python


"""



reciver=email

port=465

sslcontext=ssl.create_default_context()

connection = smtplib.SMTP_SSL("smptprotonmail.com",port,context=sslcontext)

connection.login(g4o3@protonmail.com,aS77785/)

connection.sendmail(email,reciver,message)

print("message sent")