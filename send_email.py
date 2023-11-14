import smtplib
import configparser as parser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import os
from dotenv import load_dotenv

load_dotenv()

account=os.getenv('account')
pw=os.getenv('password')

def send_auth_email(email,auth_url):
    reg = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(reg,email):

        smtp=smtplib.SMTP_SSL('smtp.gmail.com',465)
        smtp.login(account,pw)

        msg=MIMEMultipart()
        msg["Subject"]="yubin-server linkedin Auth request!"
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
