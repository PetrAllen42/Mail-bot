from dotenv import load_dotenv
import os

load_dotenv()
LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')
print(LOGIN_PASSWORD)