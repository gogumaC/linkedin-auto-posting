import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
from config import config

account=config.get('account')
pw=config.get('password')
email=config.get("client_email")

smtp=smtplib.SMTP_SSL('smtp.gmail.com',465)
smtp.login(account,pw)

reg = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def send_auth_email(auth_url):

    if re.match(reg,email):

        msg=MIMEMultipart()
        msg["Subject"]="linkedin Auth request!"
        msg["From"]=account
        msg["To"]=email

        content=f"Please click the below url, and login again.\n\n{auth_url}"
        content_part=MIMEText(content,"plain")
        msg.attach(content_part)
        smtp.sendmail(account,email,msg.as_string())

        smtp.quit()
        print(f"email sended!\n\n")
    else :
        print("email format not valid")

def send_posing_complete_email(posting_title,link):

    if re.match(reg,email):

        msg=MIMEMultipart()
        msg["Subject"]=f"Upload Posting to LinkedIn "
        msg["From"]=account
        msg["To"]=email

        content=f"Uploading Posting to LinkedIn Successfully : {posting_title} \n{link}"
        content_part=MIMEText(content,"plain")
        msg.attach(content_part)
        smtp.sendmail(account,email,msg.as_string())

        smtp.quit()
        print(f"posting complete email sended!\n\n")
    else :
        print("email format not valid")

def send_posing_fail_email(posting_title,code,text):
    
    if re.match(reg,email):

        msg=MIMEMultipart()
        msg["Subject"]=f"Fail Posting to LinkedIn"
        msg["From"]=account
        msg["To"]=email

        content=f"Fail Uploading Posting to LinkedIn : {posting_title} \n\ncode: {code} \ntext: {text}"
        content_part=MIMEText(content,"plain")
        msg.attach(content_part)
        smtp.sendmail(account,email,msg.as_string())

        smtp.quit()
        print(f"posting fail email sended!\n\n")
    else :
        print("email format not valid")