from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
PATH_TO_EMAILS = os.getenv('PATH_TO_EMAILS')
PATH_TO_EMPTY = os.getenv('PATH_TO_EMPTY')
PATH_TO_TABLE = os.getenv('PATH_TO_TABLE')

sender = "peta.kamenik@gmail.com"
subject = "Test"
txt = "ahoj"
path = PATH_TO_EMAILS
path2 = PATH_TO_EMPTY
list_attachments_path = [PATH_TO_TABLE]

msg0 = MIMEMultipart()
msg0['From'] = sender
msg0['Subject'] = subject
msg0.attach(MIMEText(txt))