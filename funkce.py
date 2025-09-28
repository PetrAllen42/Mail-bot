import smtplib
from data_file import *  
from email.mime.application import MIMEApplication
from os.path import basename
from dotenv import load_dotenv
import os

load_dotenv()
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')

class Converter:
    def __init__(self, file_path, data_list = None):
        self.file_path = file_path
        self.data_list = data_list

    def convertToList(self):
        with open(self.file_path, "r") as f:
            data = f.read()
            data_into_list = data.split("\n")
        return data_into_list
    
    def ConvertToFile(self):
        with open(self.file_path, "w") as f:
            for i in self.data_list:
                f.write(i + "\n")

class MailSender:
    def __init__(self, sender, receiver, text):
        self.sender = sender
        self.receiver = receiver
        self.text = text
    
    def sendmsg(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(self.sender, LOGIN_PASSWORD)

        server.sendmail(self.sender, self.receiver, str(self.text))
        print("email has been sent")

def textfile_to_list(path):
    t = Converter(path)
    data_list = t.convertToList()
    return data_list

def add_attachment(list, msg):
    for f in list:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name = basename(f))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)
    return msg

def send(data_list, msg):
    msg1 = add_attachment(list_attachments_path, msg)
    for i in data_list:
            m = MailSender(sender, i, msg1) 
            m.sendmsg()

def list_to_textfile(path):
    data_list = textfile_to_list(path)
    t = Converter(path2, data_list)
    t.ConvertToFile()