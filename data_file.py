from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "peta.kamenik@gmail.com"
subject = "Test"
txt = "ahoj"
path = "C:\\Users\petra\Documents\Python\Vzdelani_budoucnosti\mailbot\email.txt"
path2 = "C:\\Users\petra\Documents\Python\Vzdelani_budoucnosti\mailbot\empty.txt"
list_attachments_path = ["C:\\Users\petra\Documents\Python\output.xlsx"]

msg0 = MIMEMultipart()
msg0['From'] = sender
msg0['Subject'] = subject
msg0.attach(MIMEText(txt))