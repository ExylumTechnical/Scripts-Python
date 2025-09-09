import smtplib
import base64
import time
import os


def send_alert(message):
    sender="" # sender email goes here
    reciever="" # recipent email goes here
    password="" # password goes here, not advised but provided as an example
    try:
        smtpObj = smtplib.SMTP(host='smtp.example.com',port=587) # server is here
        smtpObj.starttls() # starting the ttls
        smtpObj.login(sender,password) # login to the server with the provided account
        nl="""
    """
        message=nl+message+nl # format the message so that it comes out looking alright
        smtpObj.sendmail(sender,reciever,message); # send the message
        tolog("sent notification successfully") # log that the message was sent successfully
        print("message sent successfully")
    except:
        tolog("notification unable to be sent at this time") # if message is unable to be sent then log that too
        print("message unable to send")
        print(message)