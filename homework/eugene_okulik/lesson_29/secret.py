import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('D_LOGIN')
password = os.getenv('D_PASSWORD')


print(f'_Login: {login}')
print(f'_Password: {password}')
